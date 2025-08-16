from rest_framework import serializers
from artisendapi.models import Post

class PostSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()  # <-- new field

    class Meta:
        model = Post
        fields = [
            "id", "title", "content", "category", "photo",
            "postal_code", "latitude", "longitude", "user",
            "display_name", "profile_image"  
        ]
        read_only_fields = ("latitude", "longitude", "user", "display_name", "profile_image")

    def get_display_name(self, obj):
        business = getattr(obj.user, "userbusiness", None)
        if business:
            return business.display_name
        return obj.user.username

    def get_profile_image(self, obj):
        user = getattr(obj.user, "user", None)
        if user and user.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(user.avatar.url)  #
            return user.avatar.url
        return None