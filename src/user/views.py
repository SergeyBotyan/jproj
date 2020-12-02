from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, DeleteView
from django.urls import reverse_lazy

from .forms import *
from .models import Profile, Adress

class UserCreationForm(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/registration.html'
    success_url = reverse_lazy('login')

@login_required
def profile_view(request):
    user = request.user
    profile = request.user.profile
    adress = request.user.adress.first()
    if not profile:
        return reverse_lazy('accounts:edit-profile')
    return render(request, 'registration/view_profile.html', {
        'user': user,
        'profile': profile,
        'adress': adress
    })




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
            return redirect('accounts:view_profile')
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

class AdmUserView(generic.DetailView):
    model = User
    template_name = 'registration/edit_profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        ed_user =  User.objects.get(pk=pk)
        profile = ed_user.profile
        adress = ed_user.adress.first()
        user = self.request.user
        context['user'] = user
        context['user_form'] = UserAdmForm(instance=ed_user)
        context['profile_form'] = ProfileAdmForm(instance=profile)
        context['adress_form'] = AdressAdmForm(instance=adress)
        session = self.request.session
        session['user_id'] = pk
        return context

class AdmUpdateProfile(generic.RedirectView):
    def get_redirect_url(self):
        user_id = self.request.session.get('user_id')
        ed_user = User.objects.get(pk=int(user_id))
        profile = ed_user.profile
        adress = ed_user.adress.first()
        user_form = UserForm(data = self.request.POST, instance=ed_user)
        profile_form = ProfileForm(data = self.request.POST, instance=profile)
        adress_form = AdressForm(data = self.request.POST, instance=adress)
        if user_form.is_valid() and profile_form.is_valid() and adress_form.is_valid():
            user_form.save()
            profile_form.save()
            adress_form.save()
            return reverse_lazy('accounts:user-list')
        else:
           messages.error(request, ('Пожалуйста, исправьте ошибки.'))
        return reverse_lazy('accounts:user-list')
    

class UserList(generic.ListView):
    model = User
    #paginate_by = 20
    template_name='registration/user_list.html'

class UserDeleteView(generic.DeleteView):
    model = User
    success_url = '/work'
    template_name = 'registration/user_confirm_delete.html'