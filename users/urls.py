from django.urls import path

from users.apps import UsersConfig
from . import views

app_name = UsersConfig.name

urlpatterns = [
    path('', views.UserLoginView.as_view(), name='login_user'),
    path('register/', views.UserRegisterView.as_view(), name='register_user'),
    path('profile/', views.UserProfileView.as_view(), name='profile_user'),
]
