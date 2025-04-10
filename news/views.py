from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from news.models import News


def index(request):
    """Отрисовка главной страницы сайта"""
    context = {
        'object_list': News.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'news/index.html', context)
