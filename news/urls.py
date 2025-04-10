from django.urls import path

from news.apps import NewsConfig
from . import views

app_name = NewsConfig.name

urlpatterns = [
    path('', views.index, name='home_page'),
]
