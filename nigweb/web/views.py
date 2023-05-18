from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from web.models import Song, Album, Artist, Genre
from nigweb.forms import *

#renders de llistes i tal
def principal(request):
    return render(request, 'web/index.html')

def all_albums(request):
    album_list = Album.objects.all()
    return render(request, 'web/album_list.html',
                  {'album_list':album_list})

def all_songs(request):
    song_list = Song.objects.all()
    return render(request, 'web/song_list.html',
                  {'song_list':song_list})

def all_artists(request):
    artist_list = Artist.objects.all()
    return render(request, 'web/artist_list.html',
                 {'artist_list':artist_list})

def all_genres(request):
    genre_list = Genre.objects.all()
    return render(request, 'web/genre.html',
                  {'genre_list':genre_list}) 

def create_genre(request):
    form = createGenreForm(request.POST)
    if form.is_valid():

        form.save()
        genre_list = Genre.objects.all()
        return render(request, 'web/genre.html', {'genre_list':genre_list})
    return render(request, 'web/create_genre.html', {'form':form})

#renders per crear instancies al model
def create_artist(request):
    form = createArtistForm(request.POST)
    if form.is_valid():

        form.save()
        artist_list = Artist.objects.all()
        return render(request, 'web/artist_list.html', {'artist_list':artist_list})
    return render(request, 'web/create_artist.html', {'form':form})

def create_album(request):
    form = createAlbumForm(request.POST)

    if form.is_valid():

        Artist.objects.filter(name=form.instance.artist)
        form.save()
        album_list = Album.objects.all()
        return render(request, 'web/album_list.html', {'album_list':album_list})
    return render(request, 'web/create_album.html', {'form':form})

def create_song(request):
    form = createSongForm(request.POST)

    if form.is_valid():

        Genre.objects.filter(genre=form.instance.genre)
        Album.objects.filter(title=form.instance.albums)
        form.save()
        song_list = Song.objects.all()
        return render(request, 'web/song_list.html',{'song_list':song_list})
    return render(request, 'web/create_song.html', {'form':form})

#renders per seleccionar instancies al model
def select_artist(request, name):
    obj = get_object_or_404(Artist.objects.all(), name = name)
    return render(request, "web/select_artist.html", {"artist": obj.name})

def select_album(request, title):
    obj = get_object_or_404(Album.objects.all(), title = title)
    return render(request, "web/select_album.html", {"album": obj.title})

def select_song(request, title):
    obj = get_object_or_404(Song.objects.all(), title = title)
    return render(request, "web/select_song.html", {"song": obj.title})

#renders per crear updatejar al model
def update_artist(request, name):
    obj = get_object_or_404(Artist, name = name)
    form = updateArtistForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        artist_list = Artist.objects.all()
        return render(request, 'web/artist_list.html', {'artist_list':artist_list})
    return render(request, 'web/update_artist.html', {'form':form})

def update_album(request, title):
    obj = get_object_or_404(Album, title = title)
    form = updateAlbumForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        album_list = Album.objects.all()
        return render(request, 'web/album_list.html', {'album_list':album_list})
    return render(request, 'web/update_album.html', {'form':form})

def update_song(request, title):
    obj = get_object_or_404(Song, title = title)
    form = updateSongForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        song_list = Song.objects.all()
        return render(request, 'web/song_list.html',{'song_list':song_list})
    return render(request, 'web/update_song.html', {'form':form})

#renders per borrar instancies al model
def delete_genre(request, genre):
    obj = get_object_or_404(Genre, genre = genre)
    if request.method =="POST":
        obj.delete()
        genre_list = Genre.objects.all()
        return render(request, 'web/genre.html', {'genre_list':genre_list})
    return render(request, "web/delete_genre.html")

def delete_artist(request, name):
    obj = get_object_or_404(Artist, name = name)
    if request.method =="POST":
        obj.delete()
        artist_list = Artist.objects.all()
        return render(request, 'web/artist_list.html', {'artist_list':artist_list})
 
    return render(request, "web/delete_artist.html")

def delete_album(request, title):
    obj = get_object_or_404(Album, title = title)
    if request.method =="POST":
        obj.delete()
        album_list = Album.objects.all()
        return render(request, 'web/album_list.html', {'album_list':album_list})
 
    return render(request, "web/delete_album.html")

def delete_song(request, title):
    obj = get_object_or_404(Song, title = title)
    if request.method =="POST":
        obj.delete()
        song_list = Song.objects.all()
        return render(request, 'web/song_list.html',{'song_list':song_list})
    return render(request, "web/delete_song.html")