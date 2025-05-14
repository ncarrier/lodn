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
    </header>
    <main>
    {% for material in materials %}
      <input type="checkbox" id="{{ material }}" name="{{ material }}" />
      <label for="{{ material }}">{{ material.capitalize() }}</label>
    {% endfor %}
    {% for category in catalog %}
      {% if catalog[category] %}
        <details open="true" class="category">
          <summary class="category_summary">
            Catégorie {{ category }}
          </summary>
          <div class="category {{ category }}">
          {% for origami in catalog[category] %}
            <div class="origami {{ ' '.join(origami.materials) }}">{{ origami.name.capitalize() }}
              <div class="photo-container"><img class="photo" src="{{ origami.name }}.png" /></div>
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
                {% if origami.paper_size != 0 %}
                  <li>taille de feuille/serviette : {{ origami.paper_size / 10 }} cm</li>
                {% endif %}
              </ul>

              <h3>Quotation</h3>
              {% if origami.quotation != 0 %}
                Durée pour 10 exemplaires : {{ origami.quotation }} minutes</li>
              {% else %}
                Quotation non disponible, nous contacter.
              {% endif %}
              <hr/>
            </div>
          {% endfor %}
        </details>
      {% endif %}
    {% endfor %}
    </main>
    <footer>
    </footer>
  </body>
</html>
