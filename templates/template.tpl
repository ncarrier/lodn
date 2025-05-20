<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>Les origamis de Nicolas</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" type="image/svg+xml" href="favicon.png">
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
        par mail.
      </p>
      <p>
        Pour ce faire c'est très simple :
        <ol>
          <li>Choisissez la taille de votre matériau (serviette, feuille...)
          <a href="#material_size">ici.</a></li>
          <li>
            Sélectionnez les matériaux à utiliser
            <a href="#material_types">ici</a>, pour n'afficher que les
            origamis compatibles.
          </li>
          <li>
            Définissez une quantité pour chaque origami que vous voulez
            <a href="#origami_catalog">ici.</a>
            Le prédevis se mettra à jour automatiquement.
          </li>
          <li>
            Envoyez-nous le devis <a id="prequote_mail">en cliquant ici.</a>
          </li>
        </a>
        </ol>
      </p>
      <p>
        Pour toute autre question, vous pouvez nous contacter
        <a href="mailto:ncarrier@live.fr?subject=Prise%20de%20contact.">par mail</a>
        ou <a href="tel:+33662804779">par téléphone.</a>
      </p>
      <p>
        <h2>Prédevis</h2>
        <strong>Attention</strong>, ce pré-devis ne tient pas compte des frais
        de déplacement, ni du coût des matériaux si ceux-ci ne sont pas fournis
        par le client.
      </p>
      <div id="prequote">
        Choisissez vos quantités pour mettre à jour le prédevis
      </div>
    </header>
    <main>
      <p>
        <h2 id="material_size">Taille du matériau</h2>
        <label for="size">Taille des feuilles / serviettes (carrées, en cm) :</label>
        <input id="size" type="number" name="size" value="40" min="5" max="50"/>
        <input type="hidden" id="hourly_rate" value="{{ hourly_rate }}">
      </p>
      <p>
        <h2 id="material_types">Types de matériau</h2>
        {% for material in materials %}
          {% if material.name in ["FABRIC_NAPKIN", "PAPER_NAPKIN"] %}
          <input class="material_checkbox" type="checkbox" id="{{ material.name }}" name="{{ material.name }}" checked />
          {% else %}
          <input class="material_checkbox" type="checkbox" id="{{ material.name }}" name="{{ material.name }}"/>
          {% endif %}
          <label for="{{ material.name }}">{{ material.value.capitalize() }}</label>
        {% endfor %}
      </p>
      <p>
        <h2 id="origami_catalog">Catalogue d'origamis</h2>
        {% for category in catalog %}
          {% if catalog[category] %}
            <details class="category" open>
              <summary class="category">
                {{ category.capitalize() }}
              </summary>
              <div id="{{ category }}_category">
                {% for origami in catalog[category] %}
                  <div class="origami {{ ' '.join(origami.materials_ids) }}">
                    <table class="origami_table">
                      <tr>
                        <td class="description">
                          <h2>{{ origami.name.capitalize() }}</h2>
                          <p class="comment">{{ origami.comment }}</p>
                          <h3>Caractéristiques</h3>
                          <ul>
                            {% if origami.diameter != 0 %}
                              <li class="diameter_text"></li>
                            {% endif %}
                            {% if origami.height != 0 %}
                              <li class="height_text"></li>
                            {% endif %}
                            {% if origami.length != 0 %}
                              <li class="length_text"></li>
                            {% endif %}
                            {% if origami.width != 0 %}
                              <li class="width_text"></li>
                            {% endif %}
                          </ul>
                          <input type="hidden" class="diameter" value="{{origami.diameter}}">
                          <input type="hidden" class="height" value="{{origami.height}}">
                          <input type="hidden" class="length" value="{{origami.length}}">
                          <input type="hidden" class="width" value="{{origami.width}}">
                          <input type="hidden" class="paper_size" value="{{origami.paper_size}}">
                          <input type="hidden" class="quotation" value="{{origami.quotation}}">
                          <input type="hidden" class="origami_name" value="{{origami.name}}">
                          <h3>Quotation</h3>
                          {% if origami.quotation != 0 %}
                            <p>Durée pour 10 exemplaires : {{ origami.quotation }} minute(s)</p>
                            <p>
                              <label for="{{ origami.name }}_num">Nombre d'origamis :</label>
                              <input class="origami_num" id="{{ origami.name }}_num" type="number" name="{{ origami.name }}_num" value="0" min="0" max="1000"/>
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
          {% endif %}
        {% endfor %}
      </p>
    </main>
    <footer>
      Ce site n'utilise pas de cookie et n'enregistre aucune donnée.
    </footer>
  </body>
</html>
