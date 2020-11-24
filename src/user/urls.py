
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


from user.views import UserChangeForm, UserCreationForm, UserLogout, update_profile

app_name = 'user'

urlpatterns = [
    path('register/', UserCreationForm.as_view(), name='register'),
    path('edit_profile/', update_profile, name='edit_profile'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', UserChangeForm.as_view(), name='view_profile'),
]
