from django.contrib import admin
from .models import Anime

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("title", "google_drive_url")
    search_fields = ("title",)
