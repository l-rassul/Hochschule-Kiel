<!DOCTYPE html>
<html>
<head>
    <title>Bewerberliste</title>
</head>
<body>
    <h1>Bewerber</h1>
    <ul>
        {% for b in bewerber %}
            <li>{{ b.vorname }} {{ b.nachname }} - Status: {{ b.status }}</li>
        {% empty %}
            <li>Keine Bewerber gefunden.</li>
        {% endfor %}
    </ul>
</body>
</html>
