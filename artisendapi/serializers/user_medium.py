from rest_framework import serializers
from artisendapi.models import Medium

class UserMediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ['id', 'business', 'medium']