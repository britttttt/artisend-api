from django.db import models
from django.contrib.auth.models import User


class ArtisendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=55)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


    @property
    def recommends(self):
        return self.__recommends

    @recommends.setter
    def recommends(self, value):
        self.__recommends = value