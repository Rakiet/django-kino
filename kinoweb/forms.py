from django.forms import  ModelForm
from .models import Move, RatingMovie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = ('username', 'password1', 'password2' )

