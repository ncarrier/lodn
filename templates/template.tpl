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
            <p class="{{ ' '.join(origami.materials) }}">{{ origami.name.capitalize() }}
              <p class="comment">{{ origami.comment }}</p>
    
            </p>
          {% endfor %}
        </details>
      {% endif %}
    {% endfor %}
    </main>
    <footer>
    </footer>
  </body>
</html>
