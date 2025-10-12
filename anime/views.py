from django.shortcuts import render
from .models import Anime

def anime_list(request):
    animes = Anime.objects.all()
    return render(request, 'anime/list.html', {'animes': animes})

def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'anime/detail.html', {'anime': anime})