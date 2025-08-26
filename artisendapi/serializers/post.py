from rest_framework import serializers
from artisendapi.models import Post, PostMedia
from .user_business import UserBusinessSerializer
from .profile import ProfileSerializer



class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['id', 'media_type', 'file', 'order']
        read_only_fields = ['id']

class PostSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(source='user.userprofile', read_only=True)
    user_business = UserBusinessSerializer  (source='user.userbusiness', read_only=True)
    media = PostMediaSerializer(many=True, read_only=True)
    
    category_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            "id", "title", "content", "category", "category_details",
            "postal_code", "latitude", "longitude", "created_at", "updated_at",
            "user", "user_profile", "user_business",
            "media"  
        ]
        read_only_fields = ("latitude", "longitude", "user", "user_profile", "user_business", "media")

    def get_category_details(self, obj):
            if obj.category:
                return {
                    'id': obj.category.id,
                    'label': obj.category.label
                    
                }
            return None