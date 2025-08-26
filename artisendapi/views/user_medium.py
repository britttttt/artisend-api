from rest_framework import viewsets
from artisendapi.models import Medium, UserMedium
from artisendapi.serializers import UserMediumSerializer
from artisendapi.serializers.medium import MediumSerializer 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class MediumViewSet(viewsets.ModelViewSet):
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserMediumViewSet(viewsets.ModelViewSet):
    serializer_class = UserMediumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserMedium.objects.filter(business__user=self.request.user)

    def perform_create(self, serializer):
        business = self.request.user.userbusiness
        serializer.save(business=business)