from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artisendapi.models import UserProfile 
from django.core.exceptions import ObjectDoesNotExist


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):  # Renamed
    url = serializers.HyperlinkedIdentityField(
        view_name='customer', lookup_field='id'
    )

    class Meta:
        model = UserProfile 
        fields = ('id', 'url', 'user')
        depth = 1


class Customers(ViewSet):
    def update(self, request, pk=None):
        try:
            user_profile = UserProfile.objects.get(user=request.auth.user)  

            user_profile.user.last_name = request.data["last_name"]
            user_profile.user.email = request.data["email"]

            user_profile.user.save()
            user_profile.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return HttpResponseServerError(str(e))