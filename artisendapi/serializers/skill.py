from rest_framework import serializers
from artisendapi.models import Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'label', 'medium']