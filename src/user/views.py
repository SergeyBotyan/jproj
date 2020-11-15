from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .forms import SignUpForm
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, View
from django.urls import reverse_lazy

class UserCreationForm(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/registration.html'
    success_url = reverse_lazy('login')

class UserChangeForm(generic.UpdateView):
    form_class=UserChangeForm
    template_name='registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class UserLogout(LogoutView):
    next_page = reverse_lazy('home')