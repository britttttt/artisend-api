from rest_framework import serializers
from artisendapi.models import UserSkill, Skill

class UserSkillSerializer(serializers.ModelSerializer):
    skill = serializers.SlugRelatedField(slug_field='label', queryset=Skill.objects.all())

    class Meta:
        model = UserSkill
        fields = ['id', 'skill']