# artisendapi/views/business_profile.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from artisendapi.models import UserBusiness
from artisendapi.serializers import UserBusinessSerializer

class BusinessProfileViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserBusinessSerializer

    def get_queryset(self):
        return UserBusiness.objects.filter(user=self.request.user)