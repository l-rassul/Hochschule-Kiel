from django.shortcuts import render
from .models import Bewerber

def bewerber_liste(request):
    bewerber = Bewerber.objects.all()
    return render(request, 'bewerber_liste.html', {'bewerber': bewerber})
