<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>Les origamis de Nicolas</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <script src="jquery-3.7.1.min.js"></script>
    <script src="lodn.js"></script>
  </head>
  <body>
    <header>
      <h1>Les origamis de Nicolas</h1>
      <p>
        Bienvenue chez les origamis de Nicolas.
        Nous proposons un service de pliage de serviettes pour les mariages,
        anniversaires, congrès d'entreprise...<br/>
        Sur cette page, vous pourrez composer un pré-devis et nous l'envoyer
        par mail
        <a href="{{ mailto }}">
          à cette addresse
        </a>, pour obtenir plus de détails.
      </p>
    </header>
    <main>
    <label for="size">Taille des feuilles / serviettes (carrées, en cm) :</label>
    <input id="size" type="number" name="size" value="40" min="0" max="50"/>
    {% for material in materials.__members__ %}
      {% if material.value in ["fabric napkin", "paper napkin"] %}
      <input class="material_checkbox" type="checkbox" id="{{ material }}" name="{{ material }}" checked />
      {% else %}
      <input class="material_checkbox" type="checkbox" id="{{ material }}" name="{{ material }}"/>
      {% endif %}
      <label for="{{ material }}">{{ material.capitalize() }}</label>
    {% endfor %}
    {% for category in catalog %}
      {% if catalog[category] %}
        <details class="category" open>
        <!-- <details class="category"> TODO -->
          <summary class="category">
            {{ category.capitalize() }}
          </summary>
          <div id="{{ category }}_category">
            {% for origami in catalog[category] %}
              <div class="origami {{ ' '.join(origami.materials_ids) }}">
                <table>
                  <tr>
                    <td class="description">
                      <em>{{ origami.name.capitalize() }}</em>
                      <p class="comment">{{ origami.comment }}</p>
                      <h3>Caractéristiques</h3>
                      <ul>
                        {% if origami.diameter != 0 %}
                          <li>diamètre : {{ origami.diameter / 10 }} cm</li>
                        {% endif %}
                        {% if origami.height != 0 %}
                          <li>hauteur : {{ origami.height / 10 }} cm</li>
                        {% endif %}
                        {% if origami.length != 0 %}
                          <li>longueur : {{ origami.length / 10 }} cm</li>
                        {% endif %}
                        {% if origami.width != 0 %}
                          <li>largeur : {{ origami.width / 10 }} cm</li>
                        {% endif %}
                      </ul>
                      <input type="hidden" name="{{origami.name}}_diameter" value="{{origami.diameter}}">
                      <input type="hidden" name="{{origami.name}}_height" value="{{origami.height}}">
                      <input type="hidden" name="{{origami.name}}_length" value="{{origami.length}}">
                      <input type="hidden" name="{{origami.name}}_paper_size" value="{{origami.paper_size}}">
                      <input type="hidden" name="{{origami.name}}_width" value="{{origami.width}}">
                      <h3>Quotation</h3>
                      {% if origami.quotation != 0 %}
                        <p>Durée pour 10 exemplaires : {{ origami.quotation }} minute(s)</p>
                        <p>
                          <label for="quantity">Nombre d'origamis :</label>
                          <input id="quantity" type="number" name="{{ origami.name }}_num" value="0" min="0" max="1000"/>
                        </p>
                      {% else %}
                        <p>Quotation non disponible, nous contacter.</p>
                      {% endif %}
                    </td>

                    <td class="photo-container">
                      <img class="photo" src="{{ origami.name }}.jpg" />
                    </td>

                  </tr>
                </table>
              </div>
            {% endfor %}
          </div>
        </details>
        <hr/>
      {% endif %}
    {% endfor %}
    </main>
    <footer>
    Ce site n'utilise pas de cookie et n'enregistre aucune données.
    </footer>
  </body>
</html>
