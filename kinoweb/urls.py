from django.urls import path
from kinoweb.views import allMovies, newMovie, editMovie, removeMovie

urlpatterns = [
    path('wszystkie-filmy/', allMovies, name="allMovies"),
    path('nowy-film/', newMovie, name="newMovie"),
    path('edytuj-film/<int:id>/', editMovie, name="editMovie"),
    path('usun-film/<int:id>/', removeMovie, name="removeMovie"),
]
