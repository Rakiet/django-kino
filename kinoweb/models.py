from django.db import models

# Create your models here.
class Move(models.Model):
    title = models.CharField(max_length=64)

