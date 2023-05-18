from django.contrib import admin

#nostre
from web.models import Song, Album, Artist, Genre

# Register your models here.

admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)

