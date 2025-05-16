<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>Les origamis de Nicolas</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
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
    <input id="size" type="number" name="size" value="36" min="0" max="50"/>
    {% for material in materials %}
      {% if material in ["fabric napkin", "paper napkin"] %}
      <input type="checkbox" id="{{ material }}" name="{{ material }}" checked />
      {% else %}
      <input type="checkbox" id="{{ material }}" name="{{ material }}" />
      {% endif %}
      <label for="{{ material }}">{{ material.capitalize() }}</label>
    {% endfor %}
    {% for category in catalog %}
      {% if catalog[category] %}
        <details class="category">
          <summary class="category_summary">
            {{ category.capitalize() }}
          </summary>
          <div class="category {{ category }}">
          {% for origami in catalog[category] %}
            <div class="origami {{ ' '.join(origami.materials) }}">
              <table>
                <tr>

                  <td>
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
              </table
              <hr/>
            </div>
          {% endfor %}
        </details>
      {% endif %}
    {% endfor %}
    </main>
    <footer>
    Ce site n'utilise pas de cookie et n'enregistre aucune données.
    </footer>
  </body>
</html>
