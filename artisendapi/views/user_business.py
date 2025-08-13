from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from artisendapi.models import UserBusiness
from artisendapi.serializers import UserBusinessSerializer

class UserBusinessViewSet(viewsets.ModelViewSet):
    serializer_class = UserBusinessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return the business for the current user
        return UserBusiness.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)