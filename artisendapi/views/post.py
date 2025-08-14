from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from artisendapi.models import Post
from artisendapi.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)
