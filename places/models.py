from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=250)
    imgs = models.ImageField()
    description_short = models.TextField()
    description_long = models.TextField()
    latitude = models.FloatField()
    longtitude = models.FloatField()

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
