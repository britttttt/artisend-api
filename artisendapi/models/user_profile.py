from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from artisendapi.utils.geolocation import geocode_postal_code

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    is_business = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto-update lat/lng when postal_code changes or is missing
        if self.postal_code and (self.latitude is None or self.longitude is None):
            lat, lon = geocode_postal_code(self.postal_code)
            self.latitude = lat
            self.longitude = lon
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s profile"

# Auto-create profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()