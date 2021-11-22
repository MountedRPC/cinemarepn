from django.db import models
from django.db.models import DateTimeField


# Create your models here.
class Cinemas(models.Model):
    name_cinemas = models.CharField(max_length=50, blank=True)
    address_cinemas = models.CharField(max_length=100, blank=True)
    image1_cinemas = models.ImageField(upload_to='media/databaseImageCinemas', blank=True)
    image2_cinemas = models.ImageField(upload_to='media/databaseImageCinemas', blank=True)
    image3_cinemas = models.ImageField(upload_to='media/databaseImageCinemas', blank=True)
    info_cinemas = models.CharField(blank=True, max_length=100)
    info_photo = models.TextField(blank=True)
    info_photo2 = models.TextField(blank=True)
    info_photo3 = models.TextField(blank=True)
    map_cinemas = models.TextField(blank=True)


class Films(models.Model):
    name_film = models.CharField(max_length=50, blank=True)
    image_film = models.ImageField(upload_to='media/databaseImageFiles', blank=True)
    video_film = models.FileField(upload_to='media/databaseVideoFilms', blank=True)
    info_film = models.TextField(blank=True)
    short_info_film = models.CharField(blank=True, max_length=100)
    genre_film = models.CharField(max_length=100, blank=True)


class Session(models.Model):
    date_session = DateTimeField(blank=True)
    ID_cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    hallnumber_session = models.IntegerField(blank=True)
    countplaces_session = models.IntegerField(blank=True)
    info_session = models.CharField(max_length=50)
    price_session = models.IntegerField()
    ID_Films = models.ForeignKey(Films, on_delete=models.CASCADE)
