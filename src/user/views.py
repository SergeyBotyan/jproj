from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import SignUpForm, UserForm, ProfileForm, AdressForm
from .models import Profile, Adress

class UserCreationForm(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/registration.html'
    success_url = reverse_lazy('login')

class UserChangeForm(generic.UpdateView):
    form_class=SignUpForm
    template_name='registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class UserLogout(LogoutView):
    next_page = reverse_lazy('home')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        adress_form = AdressForm(request.POST, instance=request.user.adress.first())
        if user_form.is_valid() and profile_form.is_valid() and adress_form.is_valid():
            user_form.save()
            profile_form.save()
            adress_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect('/')
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user = request.user
        profile = request.user.profile
        adress = request.user.adress.first()
        if not profile:
            new_profile = Profile.objects.create(
                user=user, 
                phone1=None, 
                phone2=None, 
                information=None)
            new_profile.save()
        if not adress:
            new_adress = Adress.objects.create(
                user=user, 
                country='Укажите страну', 
                sity='Укажите город', 
                post_index=None, 
                adress='Укажите адрес')
            new_adress.save()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        adress_form = AdressForm(instance=request.user.adress.first())
    return render(request, 'registration/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'adress_form': adress_form
    })