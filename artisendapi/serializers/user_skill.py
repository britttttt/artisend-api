from rest_framework import serializers
from artisendapi.models import Skill

class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','businessId','skill']