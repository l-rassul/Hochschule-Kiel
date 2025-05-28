from django.db import models

class Fachbereich(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bewerber(models.Model):
    STATUS_CHOICES = [
        ('eingegangen', 'Eingegangen'),
        ('abgelehnt', 'Abgelehnt'),
    ]

    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    geburtsdatum = models.DateField()
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    bewerbungsdatum = models.DateField(auto_now_add=True)
    gewünschter_fachbereich = models.ForeignKey(Fachbereich, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='eingegangen')

    def __str__(self):
        return f"{self.vorname} {self.nachname}"
