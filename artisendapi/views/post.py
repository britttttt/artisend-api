from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from artisendapi.models.post import Post
from artisendapi.serializers.post import PostSerializer
from artisendapi.utils.geomath import haversine
from artisendapi.utils.geolocation import geocode_postal_code

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]  # <-- added JSONParser

    def get_queryset(self):
            queryset = Post.objects.all().order_by("-created_at")
            user_id = self.request.query_params.get("user", None)
            if user_id:
                queryset = queryset.filter(user__id=user_id)
            return queryset
    
    def perform_create(self, serializer):
        postal_code = self.request.data.get("postal_code") or getattr(
            self.request.user.userprofile, "postal_code", None
        )
        lat, lon = None, None
        try:
            lat, lon = geocode_postal_code(postal_code)
        except Exception:
            lat, lon = None, None 

        serializer.save(
            user=self.request.user,
            latitude=lat,
            longitude=lon
        )

    @action(detail=False, methods=["get"])
    def nearby(self, request):
        radius = float(request.query_params.get("radius", 25))
        user = request.user
        lat, lon = getattr(user.userprofile, "latitude", None), getattr(user.userprofile, "longitude", None)

        if lat is None or lon is None:
            return Response({"error": "User location not set"}, status=400)

        posts = [
            post for post in Post.objects.exclude(latitude=None).exclude(longitude=None)
            if haversine(lat, lon, post.latitude, post.longitude) <= radius
        ]

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)