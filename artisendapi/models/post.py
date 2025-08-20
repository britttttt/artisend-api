from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="Untitled")
    content = models.TextField()
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='posts'
    )
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        """Ensure limits on media attachments"""
        media_items = self.media.all()
        if media_items.count() > 5:
            raise ValidationError("Maximum 5 uploads per post")

        video_count = media_items.filter(media_type='video').count()
        audio_count = media_items.filter(media_type='audio').count()

        if video_count > 1:
            raise ValidationError("Only one video per post")
        if audio_count > 1:
            raise ValidationError("Only one audio file per post")