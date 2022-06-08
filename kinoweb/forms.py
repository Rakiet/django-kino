from django.forms import  ModelForm
from .models import Move

class MoveForm(ModelForm):
    class Meta:
        model = Move
        fields = ['title', 'year', 'description', 'premiere', 'imdb_rating', 'poster']

