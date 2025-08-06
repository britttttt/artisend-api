from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()