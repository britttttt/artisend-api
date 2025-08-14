

from rest_framework import viewsets
from artisendapi.models import Skill, UserSkill
from artisendapi.serializers import UserSkillSerializer, SkillSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserSkillViewSet(viewsets.ModelViewSet):
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserSkill.objects.filter(business__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()