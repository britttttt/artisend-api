from django.db import models
from django.contrib.auth.models import User

class UserBusiness(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userbusiness")
    bio = models.TextField(blank=True)
    business_email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    business_address = models.CharField(max_length=255, blank=True)
    social_link = models.CharField(max_length=200, blank=True)
    commissions_open = models.BooleanField(default=False)
    banner_img = models.ImageField(upload_to='banners/', null=True, blank=True)

    # Link to mediums and skills by string references
    mediums = models.ManyToManyField('Medium', blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return f"{self.user.username}'s business"