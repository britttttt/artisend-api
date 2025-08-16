
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from artisendapi.models import UserProfile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    postal_code = serializers.CharField(source='userprofile.postal_code', allow_blank=True)
    profile_pic = serializers.ImageField(source='userprofile.profile_pic', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'postal_code', 'profile_pic']

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get current user's data"""
        user = request.user
        # Get or create user profile if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(user=user)
        
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    def update(self, request, pk=None, **kwargs):
        """Update current user's data"""
        user = request.user
        profile, created = UserProfile.objects.get_or_create(user=user)
        
        # Update user fields
        user.username = request.data.get('username', user.username)
        user.email = request.data.get('email', user.email)
        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)
        user.save()
        
        # Update profile fields
        profile.postal_code = request.data.get('postal_code', profile.postal_code)
        if 'avatar' in request.FILES:
            profile.profile_pic = request.FILES['avatar']
        profile.save()
        
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None, **kwargs):
        """Handle partial updates (PATCH requests)"""
        return self.update(request, pk, **kwargs)