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

    path('artists/<str:name>', wv.select_artist, name="select_artist"),
    path('albums/<str:title>', wv.select_album, name="select_album"),
    path('songs/<str:title>', wv.select_song, name="select_song"),

    path('genres/create_genre/', wv.create_genre, name='create_genre'),
    path('artists/create_artist/', wv.create_artist, name='create_artist'),
    path('albums/create_album/', wv.create_album, name='create_album'),
    
    path('songs/create_song/', wv.create_song, name='create_song'),

    path('artists/<str:name>/update/', wv.update_artist, name='update_artist'),
    path('albums/<str:title>/update/', wv.update_album, name='upate_album'),
    path('songs/<str:title>/update/', wv.update_song, name='update_song'),

    path('genres/<str:genre>/', wv.delete_genre, name='delete_genre'),
    path('artists/<str:name>/delete/', wv.delete_artist, name='delete_artist'),
    path('albums/<str:title>/delete/', wv.delete_album, name='delete_album'),
    
    path('songs/<str:title>/delete/', wv.delete_song, name='delete_song'),

]
