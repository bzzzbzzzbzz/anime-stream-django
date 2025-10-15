from django.shortcuts import render, get_object_or_404
from .models import Anime


def anime_list(request):
    animes = Anime.objects.all().order_by('-created_at')
    return render(request, 'anime/anime_list.html', {'animes': animes})


def anime_detail(request, pk):
    anime = get_object_or_404(Anime, pk=pk)

    # Улучшенная проверка Google Drive
    video_url = anime.video
    is_google_drive = 'drive.google.com' in video_url

    # Если это Google Drive, убедимся что ссылка правильная
    if is_google_drive and '/view' in video_url:
        video_url = video_url.replace('/view', '/preview')

    context = {
        'anime': anime,
        'is_google_drive': is_google_drive,
    }
    return render(request, 'anime/anime_detail.html', context)