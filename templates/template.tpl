<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>Les origamis de Nicolas</title>
    <link rel="stylesheet" href="style.css">
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
        <details class="category">
          <summary class="category_summary">
            <h2>Catégorie {{ category }}</h2>
          </summary>
          <div class="{{ category }}">
          {% for origami in catalog[category] %}
            <div class="{{ ' '.join(origami.materials) }}">{{ origami.name.capitalize() }}
              <p class="comment">{{ origami.comment }}</p>
              <img src="{{ origami.name }}.png" />
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
