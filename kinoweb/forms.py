from django.forms import  ModelForm
from .models import Move, RatingMovie

class MoveForm(ModelForm):
    class Meta:
        model = Move
        fields = ['title', 'year', 'description', 'premiere', 'imdb_rating', 'poster']

class RatingForm(ModelForm):
    class Meta:
        model = RatingMovie
        fields = ['textReview', 'stars']

