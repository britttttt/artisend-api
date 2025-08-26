from rest_framework import serializers
from artisendapi.models import Medium
from artisendapi.serializers.skill import SkillSerializer 

class MediumSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True) 

    class Meta:
        model = Medium
        fields = ['id', 'label', 'skills']