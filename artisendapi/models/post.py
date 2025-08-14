from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

from math import radians, cos, sin, asin, sqrt
from artisendapi.models import Post

def get_nearby_posts(user, radius_km=25):
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0  # Earth radius in km
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        return R * c

    user_lat = getattr(user, "latitude", None)
    user_lon = getattr(user, "longitude", None)

    if user_lat is None or user_lon is None:
        return Post.objects.none()

    posts = Post.objects.exclude(latitude__isnull=True, longitude__isnull=True)
    nearby_posts = [
        post for post in posts
        if haversine(user_lat, user_lon, post.latitude, post.longitude) <= radius_km
    ]
    return nearby_posts