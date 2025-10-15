from django.shortcuts import render, get_object_or_404
from .models import Anime

def anime_list(request):
    animes = Anime.objects.all().order_by('-created_at')
    return render(request, 'anime/anime_list.html', {'animes': animes})

def anime_detail(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    return render(request, 'anime/anime_detail.html', {'anime': anime})