from rest_framework import serializers
from artisendapi.models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'profile_pic', 'is_business', 'postal_code', 'latitude', 'longitude'
        ]
        read_only_fields = ['id', 'username', 'latitude', 'longitude']