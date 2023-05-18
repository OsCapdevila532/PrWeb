from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from web.models import Song, Album, Artist, Genre
from nigweb.forms import *

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
        return render(request, 'web/index.html')
    return render(request, 'web/create_genre.html', {'form':form})
        
def create_artist(request):
    form = createArtistForm(request.POST)
    if form.is_valid():

        form.save()
        return render(request, 'web/index.html')
    return render(request, 'web/create_artist.html', {'form':form})

def create_album(request):
    form = createAlbumForm(request.POST)

    if form.is_valid():

        Artist.objects.filter(name=form.instance.artist)
        form.save()
        return render(request, 'web/index.html')
    return render(request, 'web/create_album.html', {'form':form})

def create_song(request):
    form = createSongForm(request.POST)

    if form.is_valid():

        Genre.objects.filter(genre=form.instance.genre)
        Album.objects.filter(album=form.instance.album)
        form.save()
        return render(request, 'web/index.html')
    return render(request, 'web/create_song.html', {'form':form})

#?
from django.shortcuts import (get_object_or_404, HttpResponseRedirect)

def update_genre(request, id):
    obj = get_object_or_404(Genre, id = id)
    form = updateGenreForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
        #return render(request, 'web/index.html')
    return render(request, 'web/update_genre.html', {'form':form})

def update_artist(request, id):
    obj = get_object_or_404(Artist, id = id)
    form = updateArtistForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
        #return render(request, 'web/index.html')
    return render(request, 'web/update_artist.html', {'form':form})

def update_album(request, id):
    obj = get_object_or_404(Album, id = id)
    form = updateAlbumForm(request.POST or None, instance = obj)

    if form.is_valid():
        #Artist.objects.filter(name=form.instance.artist)
        form.save()
        return HttpResponseRedirect("/"+id)
        #return render(request, 'web/index.html')
    return render(request, 'web/update_album.html', {'form':form})

def update_song(request, id):
    obj = get_object_or_404(Song, id = id)
    form = updateSongForm(request.POST or None, instance = obj)

    if form.is_valid():
        #Genre.objects.filter(genre=form.instance.genre)
        #Album.objects.filter(album=form.instance.album)
        form.save()
        return HttpResponseRedirect("/"+id)
        #return render(request, 'web/index.html')
    return render(request, 'web/update_song.html', {'form':form})

def delete_genre(request, id):
    obj = get_object_or_404(Genre, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
        #return render(request, 'web/index.html')
 
    return render(request, "deleteGenre.html")

def delete_artist(request, id):
    obj = get_object_or_404(Artist, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
        #return render(request, 'web/index.html')
 
    return render(request, "deleteArtist.html")

def delete_album(request, id):
    obj = get_object_or_404(Album, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
        #return render(request, 'web/index.html')
 
    return render(request, "deleteAlbum.html")

def delete_song(request, id):
    obj = get_object_or_404(Song, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
        #return render(request, 'web/index.html')
 
    return render(request, "deleteSong.html")

# class ArtistCreateView(CreateView):
#     model = Artist
#     fields = ['name', 'genres']
#     template_name = 'create_artist.html'
#     success_url = '/'

# class AlbumCreateView(CreateView):
#     model = Album
#     fields = ['title', 'artist', 'genres']
#     template_name = 'create_album.html'
#     success_url = '/'

# class SongCreateView(CreateView):
#     model = Song
#     fields = ['title', 'release_date', 'genre', 'albums', 'artists']
#     template_name = 'create_song.html'
#     success_url = '/'


# def get_queryset(self):         #Login per update i delete
#         qs = super().get_queryset()
#         return qs.filter(user=self.request.user)


# class GenreUpdateView(LoginRequiredMixin, UpdateView):
#     model = Genre
#     fields = ['genre']
#     template_name = 'update_genre.html'
#     success_url = '/'

# class GenreDeleteView(LoginRequiredMixin, DeleteView):
#     model = Genre
#     template_name = 'delete_genre.html'
#     success_url = '/'


# class ArtistUpdateView(LoginRequiredMixin, UpdateView):
#     model = Artist
#     fields = ['artist']
#     template_name = 'update_artist.html'
#     success_url = '/'

# class ArtistDeleteView(LoginRequiredMixin, DeleteView):
#     model = Artist
#     template_name = 'delete_artist.html'
#     success_url = '/'


# class AlbumUpdateView(LoginRequiredMixin, UpdateView):
#     model = Album
#     fields = ['album']
#     template_name = 'update_album.html'
#     success_url = '/'

# class AlbumDeleteView(LoginRequiredMixin, DeleteView):
#     model = Album
#     template_name = 'delete_album.html'
#     success_url = '/'


# class SongUpdateView(LoginRequiredMixin, UpdateView):
#     model = Song
#     fields = ['song']
#     template_name = 'update_song.html'
#     success_url = '/'

# class SongDeleteView(LoginRequiredMixin, DeleteView):
#     model = Song
#     template_name = 'delete_song.html'
#     success_url = '/'