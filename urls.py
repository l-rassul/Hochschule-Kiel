from django.urls import path
from core import views

urlpatterns = [
    path('bewerber/', views.bewerber_liste, name='bewerber_liste'),
    # ... andere urls
]
