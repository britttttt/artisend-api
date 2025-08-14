from rest_framework import serializers
from artisendapi.models import Post
from artisendapi.utils.geolocation import geocode_postal_code

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id", "title", "content", "category", "photo", 
            "postal_code", "latitude", "longitude", "user"
        ]
        read_only_fields = ("latitude", "longitude", "user")

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["user"] = request.user

            postal_code = validated_data.get("postal_code") or request.user.userprofile.postal_code
            if postal_code:
                lat, lng = geocode_postal_code(postal_code)
                validated_data["latitude"] = lat
                validated_data["longitude"] = lng

        return super().create(validated_data)