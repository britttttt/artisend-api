# models/user_business.py
from django.db import models

from django.contrib.auth.models import User

class UserBusiness(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    banner_img = models.ImageField(upload_to='banners/', null=True, blank=True)
    bio = models.TextField(max_length=500)
    business_email = models.EmailField()
    phone = models.CharField(max_length=15)
    business_address = models.CharField(max_length=200)
    social_link = models.URLField(max_length=200, blank=True)
    commissions_open = models.BooleanField(default=False)

    mediums = models.ManyToManyField('artisendapi.Medium', through='artisendapi.UserMedium')
    skills = models.ManyToManyField('artisendapi.Skill', blank=True, related_name='businesses')