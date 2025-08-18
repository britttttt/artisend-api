from rest_framework import serializers
from artisendapi.models import Post
from .user_business import UserBusinessSerializer
from .profile import ProfileSerializer

class PostSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(source='user.userprofile', read_only=True)
    user_business = UserBusinessSerializer  (source='user.userbusiness', read_only=True)
    class Meta:
        model = Post
        fields = [
            "id", "title", "content", "category", "photo",
            "postal_code", "latitude", "longitude", "user", "user_business", "user_profile"  
        ]
        read_only_fields = ("latitude", "longitude", "user_business", "user_profile")

   