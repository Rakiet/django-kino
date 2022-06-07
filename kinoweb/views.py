from django.shortcuts import render
from .models import Move
from django.http import HttpResponse
# Create your views here.
def allMovies(request):
    allMOviesFromDB = Move.objects.all()
    return render(request, 'filmy.html',{'movies': allMOviesFromDB})