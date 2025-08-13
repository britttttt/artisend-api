from rest_framework import viewsets, status
from rest_framework.response import Response
from artisendapi.models import UserBusiness
from artisendapi.serializers import UserBusinessSerializer

class UserBusinessViewSet(viewsets.ModelViewSet):
    queryset = UserBusiness.objects.all()
    serializer_class = UserBusinessSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(user=request.user)
        return Response(
            {"success": True, "id": instance.id},
            status=status.HTTP_201_CREATED
        )