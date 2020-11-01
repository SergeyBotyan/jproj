from django import forms
from . import models


class CreateAuthorForm(forms.ModelForm):
  
    class Meta:
        model = models.Author
        fields = ('__all__') 

class CreateGenreForm(forms.ModelForm):
  
    class Meta:
        model = models.Genre
        fields = ('__all__')

class CreateSeriesForm(forms.ModelForm):
  
    class Meta:
        model = models.Book_series
        fields = ('__all__')

class CreatePublisherForm(forms.ModelForm):
  
    class Meta:
        model = models.Publisher
        fields = ('__all__')