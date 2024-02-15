from django import forms
from .models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['movie_title','poster_img','desc','release_date','actors','category','ylink']