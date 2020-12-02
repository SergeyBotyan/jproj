from django import forms
from django.contrib.auth.models import User
from .models import Profile, Adress


class SignUpForm(forms.ModelForm):
  
    class Meta:
        model = User
        fields = (
        'username', 
        'email', 
        'first_name', 
        'last_name'
        ) 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone1', 'phone2', 'information')

class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ('country', 'sity', 'post_index', 'adress')

class UserAdmForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_staff')

class ProfileAdmForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone1', 'phone2', 'information')

class AdressAdmForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ('country', 'sity', 'post_index', 'adress')