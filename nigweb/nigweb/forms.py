from django import forms
from web.models import *

class createGenreForm(forms.ModelForm):
    
    class Meta:
        model = Genre
        fields = ['genre']

class createArtistForm(forms.ModelForm):
    
    class Meta:
        model = Artist
        fields = ['name', 'genres']
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)
    
class createAlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ['title', 'genres', 'artist']
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

class createSongForm(forms.ModelForm):
    
    class Meta:
        model = Song
        fields = ['title', 'release_date', 'genre', 'albums', 'artists']
    release_date = forms.DateField()
    artists = forms.ModelMultipleChoiceField(queryset=Artist.objects.all(), widget=forms.CheckboxSelectMultiple)

### ?
class updateGenreForm(forms.ModelForm):
    
    class Meta:
        model = Genre
        fields = ['genre']

class updateArtistForm(forms.ModelForm):
    
    class Meta:
        model = Artist
        fields = ['name', 'genres']
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

class updateAlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ['title', 'genres', 'artist']
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

class updateSongForm(forms.ModelForm):
    
    class Meta:
        model = Song
        fields = ['title', 'release_date', 'genre', 'albums', 'artists']
    release_date = forms.DateField()
    artists = forms.ModelMultipleChoiceField(queryset=Artist.objects.all(), widget=forms.CheckboxSelectMultiple)

class deleteGenreForm(forms.ModelForm):
    
    class Meta:
        model = Genre
        fields = ['genre']
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())

class deleteArtistForm(forms.ModelForm):
    
    class Meta:
        model = Artist
        fields = ['name']
    name = forms.ModelChoiceField(queryset=Artist.objects.all())

class deleteAlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ['title']
    title = forms.ModelMultipleChoiceField(queryset=Album.objects.all(), widget=forms.CheckboxSelectMultiple)

class deleteSongForm(forms.ModelForm):
    
    class Meta:
        model = Song
        fields = ['title']
    title = forms.ModelChoiceField(queryset=Song.objects.all())
### ?