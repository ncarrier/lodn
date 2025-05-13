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
    {% for category in data %}
      <details class="category">
        <summary class="category_summary">
          <h2>Catégorie {{ category }}</h2>
        </summary>
      <div class="{{ category }}">
      {% for origami in data[category] %}
        <p class="{{ ' '.join(origami.materials) }}">{{ origami.name }}</p>
      {% endfor %}
      </details>
    {% endfor %}
    </main>
    <footer>
    </footer>
  </body>
</html>
