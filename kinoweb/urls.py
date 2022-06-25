from django.urls import path
from kinoweb.views import allMovies, newMovie, editMovie, removeMovie, singleMovie, signup

urlpatterns = [
    path('wszystkie-filmy/', allMovies, name="allMovies"),
    path('nowy-film/', newMovie, name="newMovie"),
    path('edytuj-film/<int:id>/', editMovie, name="editMovie"),
    path('usun-film/<int:id>/', removeMovie, name="removeMovie"),
    path('film/<int:id>/', singleMovie, name="singleMovie"),
    path('rejestracja/', signup, name='signup'),
]
