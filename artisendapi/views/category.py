from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from artisendapi.models import Category
from artisendapi.serializers import CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by("label")
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]