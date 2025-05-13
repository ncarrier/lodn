<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Mon Site{% endblock %}</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>{{ titre }} Bienvenue {{ utilisateur }}</h1>
    </header>
    <main>
    </main>
    <footer>
    </footer>
</body>
</html>
