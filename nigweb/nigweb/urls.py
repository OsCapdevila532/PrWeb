"""
URL configuration for nigweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import web.views as wv

urlpatterns = [
    path('', wv.principal, name="Principal"),
    path('admin/', admin.site.urls),
    path('albums/', wv.all_albums, name="albums"),
    path('songs/', wv.all_songs, name="songs"),
    path('artists/', wv.all_artists, name="artists"),
    path('genres/', wv.all_genres, name="genres"),

    path('genres/create_genre/', wv.create_genre, name='create_genre'),
    path('artists/create_artist/', wv.create_artist, name='create_artist'),
    path('albums/create_album/', wv.create_album, name='create_album'),
    path('songs/create_song/', wv.create_song, name='create_song'),

    path('genre/update/', wv.GenreUpdateView.as_view(), name='update_genre'),
    path('artist/update/', wv.ArtistUpdateView.as_view(), name='update_artist'),
    path('album/update/', wv.AlbumUpdateView.as_view(), name='upate_album'),
    path('song/update/', wv.SongUpdateView.as_view(), name='update_song'),

    # path('genre/delete/', wv.GenreDeleteView.as_view(), name='delete_genre'),
    # path('artist/delete/', wv.ArtistDeleteView.as_view(), name='delete_artist'),
    # path('album/delete/', wv.AlbumDeleteView.as_view(), name='delete_album'),
    # path('song/delete/', wv.SongDeleteView.as_view(), name='delete_song'),
]
