from django.contrib import admin
from .models import Anime


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'poster', 'video')

    def save_model(self, request, obj, form, change):
        if not obj.video:
            from django.core.exceptions import ValidationError
            raise ValidationError("Поле 'Видео' обязательно для заполнения")
        super().save_model(request, obj, form, change)