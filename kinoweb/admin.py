from django.contrib import admin
from .models import Move, ExtraInfoToMovie, RatingMovie
# Register your models here.

admin.site.register(Move)
admin.site.register(ExtraInfoToMovie)
admin.site.register(RatingMovie)