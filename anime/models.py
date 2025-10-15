from django.db import models
from django.utils import timezone


class Anime(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    poster = models.ImageField(upload_to='posters/', verbose_name="Постер")
    video = models.URLField(verbose_name="Ссылка на видео", help_text="Используйте ссылку Google Drive для встраивания")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"