from django.forms import  ModelForm
from .models import Move, RatingMovie

class MoveForm(ModelForm):
    class Meta:
        model = Move
        fields = ['title', 'year', 'description', 'premiere', 'imdb_rating', 'poster']

class RatingForm(ModelForm):
    class Meta:
        model = RatingMovie
        labels = {
            "textReview": "Recenzja",
            "stars": "Ocena",
            "userName": "Nazwa użytkownika"
        }
        fields = ['userName', 'textReview', 'stars']

