
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


from user.views import profile_view, UserCreationForm, UserDeleteView, AdmUserView, UserUpdateProfile
from user.views import UserLogout, update_profile, UserList, AdmUpdateProfile, UserView

app_name = 'user'

urlpatterns = [
    path('register/', UserCreationForm.as_view(), name='register'),
    path('edit-profile/<int:pk>', UserView.as_view(), name='edit-profile'),
    path('profile/user-update/', UserUpdateProfile.as_view(), name='user-update-profile'),
    path('edit-profile-adm/<int:pk>', AdmUserView.as_view(), name='edit-profile-adm'),
    path('profile/adm-update/', AdmUpdateProfile.as_view(), name='adm-update-profile'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', profile_view, name='view_profile'),
    path('user-list/', UserList.as_view(), name='user-list'),
    path('user-delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
]
