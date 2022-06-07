from django.urls import path
from kinoweb.views import allMovies

urlpatterns = [
    path('wszystkie-filmy/', allMovies)
]
