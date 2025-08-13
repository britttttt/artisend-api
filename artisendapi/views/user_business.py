from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import UserBusiness
from .serializers import UserBusinessSerializer

class UserBusinessViewSet(viewsets.ModelViewSet):
    queryset = UserBusiness.objects.all()
    serializer_class = UserBusinessSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(
            {"success": True, "id": instance.id},
            status=status.HTTP_201_CREATED
        )