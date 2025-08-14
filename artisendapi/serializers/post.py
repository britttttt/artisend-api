from rest_framework import serializers
from artisendapi.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'userId', 'content', 'latitude', 'longitude']
        read_only_fields = ['id', 'userId']  # user is set from request

    def create(self, validated_data):
        # Assign the logged-in user as the post author
        user = self.context['request'].user
        return Post.objects.create(userId=user, **validated_data)