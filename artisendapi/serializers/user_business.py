# serializers/user_business.py
from rest_framework import serializers
from artisendapi.models import UserBusiness
from .user_medium import UserMediumSerializer
from .user_skill import UserSkillSerializer

class UserBusinessSerializer(serializers.ModelSerializer):
    mediums = UserMediumSerializer(many=True, read_only=True)
    skills = UserSkillSerializer(many=True, read_only=True)

    class Meta:
        model = UserBusiness
        fields = [
            'id', 'user', 'bio', 'business_email', 'phone', 'business_address',
            'social_link', 'commissions_open', 'banner_img', 'mediums', 'skills'
        ]
        read_only_fields = ['id', 'user']