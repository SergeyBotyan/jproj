
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


from user.views import UserChangeForm, UserCreationForm, UserLogout

urlpatterns = [
    path('register/', UserCreationForm.as_view(), name='register'),
    path('edit_profile/', UserChangeForm.as_view(), name='edit_profile'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', UserChangeForm.as_view(), name='edit_profile'),
]
