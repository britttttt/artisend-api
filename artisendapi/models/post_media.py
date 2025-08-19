from django.db import models
from django.contrib.auth.models import User
from .post import Post

class PostMedia(models.Model):
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio')])
    file = models.FileField(upload_to='post_media/')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)