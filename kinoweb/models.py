from django.db import models

# Create your models here.
class Move(models.Model):
    title = models.CharField(max_length=64, blank=False)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

    def __str__(self):
        return self.titleWithYear()

    def titleWithYear(self):
        return "{} ({})".format(self.title, self.year)