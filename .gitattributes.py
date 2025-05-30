'''
<!-- Start der Hochschulbewerbung Webanwendung: index.html -->
<!DOCTYPE html>
<html lang="de">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Hochschulbewerbung</title>
 <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
 <!-- Header -->
 <header class="bg-blue-800 text-white p-6">
 <h1 class="text-3xl font-bold">Willkommen zur Hochschulbewerbung</h1>
 <p>Gestalte deine Zukunft  bewirb dich jetzt online!</p>
    </header>

    <!-- Startseite mit Werbetexten -->
<section class="p-8">
    <h2 class="text-2xl font-semibold mb-4">Warum unsere Hochschule?</h2>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div>
        <img src="hochschule.jpg" alt="Campusbild" class="rounded shadow">
      </div>
      <div>
        <p class="text-gray-700">Unsere Hochschule steht für Innovation, Vielfalt und exzellente Lehre. Mit modernen Studiengängen und praxisnaher Ausbildung bist du bestens für die Zukunft vorbereitet.</p>
      </div>
    </div>
  </section>

  <!-- Bewerbungsformular-Start (Mehrschritt-Formular durch JS ergänzbar) -->
  <section class="p-8 bg-white shadow rounded">
    <h2 class="text-xl font-semibold mb-4">Bewerbungsformular</h2>
    <form id="bewerbungsformular" method="POST" action="/submit_application">
      <div class="mb-4">
        <label class="block mb-1 font-medium">Studiengang</label>
        <select name="studiengang" class="w-full border rounded p-2">
          <option>Informatik</option>
          <option>BWL</option>
          <option>Maschinenbau</option>
          <option>Medienwissenschaft</option>
        </select>
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Abschluss</label>
        <label><input type="radio" name="abschluss" value="Bachelor"> Bachelor</label>
        <label class="ml-4"><input type="radio" name="abschluss" value="Master"> Master</label>
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Sprache</label>
        <select name="sprache" class="w-full border rounded p-2">
          <option>Deutsch</option>
          <option>Englisch</option>
        </select>
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">Name</label>
        <input type="text" name="name" class="w-full border rounded p-2">
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium">E-Mail</label>
        <input type="email" name="email" class="w-full border rounded p-2">
      </div>

      <button type="submit" class="bg-blue-700 text-white px-4 py-2 rounded hover:bg-blue-800">Absenden</button>
    </form>
  </section>

  <!-- Footer -->
  <footer class="text-center p-4 mt-8 bg-gray-200">
    <p>&copy; 2025 Hochschule Bewerbung. Alle Rechte vorbehalten.</p>
  </footer>
</body>
</html>

<!-- Hinweis: Backend (z.B. mit Django oder PHP) speichert Formulardaten in Datenbank, implementiert Rollenverwaltung und E-Mail-Versand. -->

<!-- KI-Code-Generierungshinweis:
Dieser HTML/Tailwind-Code wurde mithilfe von ChatGPT generiert. Die Struktur orientiert sich an modernen Hochschul-Webseiten (z.B. RWTH Aachen, LMU München).
Er wurde manuell überarbeitet und kommentiert. Es fehlen interaktive Vue.js-Komponenten und serverseitige Logik, die im Backend ergänzt werden.
Die gewählte Gestaltung fördert gute User Experience und ist responsive.
Die Barrierefreiheit kann noch durch ARIA-Tags und Fokus-Indikatoren verbessert werden. -->

'''