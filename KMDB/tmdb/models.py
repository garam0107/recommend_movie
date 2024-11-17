from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=200, blank= True, null= True)

class Genre(models.Model):
    name = models.CharField(max_length=50) 

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True)  
    popularity = models.FloatField()
    vote_count = models.IntegerField()  
    vote_average = models.FloatField()  
    overview = models.TextField()   
    poster_path = models.CharField(max_length=200, blank=True)   #이미지
    backdrop_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, blank=True)
    youtube_key = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, blank= True)
    director = models.CharField(max_length=100, blank=True)
