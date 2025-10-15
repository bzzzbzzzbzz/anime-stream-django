from django.db import models

class Anime(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", blank=True)
    google_drive_url = models.URLField("Ссылка на Google Диск", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_embed_url(self):
        """
        Возвращает корректную ссылку для встраивания видео с Google Drive.
        Работает и для /file/d/.../view, и для uc?export=download&id=...
        """
        if not self.google_drive_url:
            return None

        import re

        # Пробуем извлечь ID из разных форматов
        patterns = [
            r"/d/([^/]+)/",  # формат /file/d/ID/
            r"id=([a-zA-Z0-9_-]+)",  # формат ?id=ID
        ]

        for pattern in patterns:
            match = re.search(pattern, self.google_drive_url)
            if match:
                file_id = match.group(1)
                return f"https://drive.google.com/file/d/{file_id}/preview"

        return None