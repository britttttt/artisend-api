from rest_framework import serializers
from artisendapi.models import UserMedium, Medium

class UserMediumSerializer(serializers.ModelSerializer):
    medium = serializers.SlugRelatedField(slug_field='label', queryset=Medium.objects.all())

    class Meta:
        model = UserMedium
        fields = ['id', 'medium']