from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.genre

class Artist(models.Model):
    name = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre)
    #songs = models.ManyToManyField(Song, null=True)

    def __str__(self) -> str:
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    albums = models.ForeignKey(Album, on_delete=models.SET_NULL,blank=True,null=True)
    artists = models.ManyToManyField(Artist)

    def __str__(self) -> str:
        return self.title
    




