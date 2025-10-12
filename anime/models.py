from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='anime_videos/')

    def __str__(self):
        return self.title