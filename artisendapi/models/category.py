from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    label = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['label']

    def __str__(self):
        return self.label