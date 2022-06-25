from .models import Move, RatingMovie
from .forms import MoveForm, RatingForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404


def allMovies(request):
    allMOviesFromDB = Move.objects.all()
    return render(request, 'filmy.html',{'movies': allMOviesFromDB})

def singleMovie(request, id):
    movie = get_object_or_404(Move, pk=id)
    coments = RatingMovie.objects.all().filter(movie_id=id)
    form = RatingForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        model_instance = form.save(commit=False)
        model_instance.movie_id = id
        model_instance.save()
        return redirect(allMovies)

    return render(request, 'singleMovie.html', {'form': form,'movie': movie,'coments': coments})

@login_required
def newMovie(request):
    isNewMovie = True
    form = MoveForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(allMovies)

    return render(request, 'movieForm.html', {'form': form,'isNewMovie': isNewMovie})

@login_required
def editMovie(request, id):
    isNewMovie = False
    movie = get_object_or_404(Move, pk=id)
    form = MoveForm(request.POST or None, request.FILES or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect(allMovies)

    return render(request, 'movieForm.html', {'form': form,'isNewMovie': isNewMovie})

@login_required
def removeMovie(request, id):
    movie = get_object_or_404(Move, pk=id)
    if request.method == "POST":
        movie.delete()
        return redirect(allMovies)

    return render(request, 'confirmDeleteMovie.html', {'movie': movie})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})