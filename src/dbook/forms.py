from django import forms
from . import models


class CreateBookForm(forms.ModelForm):
  
    class Meta:
        model = models.Book
        fields = ('__all__')
        
        



   

