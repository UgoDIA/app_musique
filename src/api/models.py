from django.db import models


class AudioFile(models.Model):
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='audio/temp')
    audio_url = models.CharField(max_length=255, blank=True)