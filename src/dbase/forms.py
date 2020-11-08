from django import forms
from . import models


class AuthorForm(forms.ModelForm):
  
    class Meta:
        model = models.Author
        fields = ('__all__') 

class GenreForm(forms.ModelForm):
  
    class Meta:
        model = models.Genre
        fields = ('__all__')

class SeriesForm(forms.ModelForm):
  
    class Meta:
        model = models.Book_series
        fields = ('__all__')

class PublisherForm(forms.ModelForm):
  
    class Meta:
        model = models.Publisher
        fields = ('__all__')