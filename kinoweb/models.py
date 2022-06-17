from django.db import models

# Create your models here.
class ExtraInfoToMovie(models.Model):

    genreMovie = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Dramat'),
        (5, 'Akcji'),
    }

    duration = models.PositiveSmallIntegerField(default=0)
    genre = models.PositiveSmallIntegerField(default=0, choices=genreMovie)

class Move(models.Model):
    title = models.CharField(max_length=64, blank=False)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

    extra = models.OneToOneField(ExtraInfoToMovie, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titleWithYear()

    def titleWithYear(self):
        return "{} ({})".format(self.title, self.year)

class RatingMovie(models.Model):
    textReview = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5, blank=True)
    movie = models.ForeignKey(Move, on_delete=models.CASCADE)


# class Comments(models.Model):
#