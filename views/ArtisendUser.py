from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from models import ArtisendUser
from django.core.exceptions import ObjectDoesNotExist


class ArtisendUserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Artisend users"""
    class Meta:
        model = ArtisendUser
        url = serializers.HyperlinkedIdentityField(
            view_name='customer', lookup_field='id'
        )
        fields = ('id', 'url', 'user')
        depth = 1


class Customers(ViewSet):

    def update(self, request, pk=None):
        """
        @api {PUT} /customers/:id PUT changes to customer profile
        @apiName UpdateCustomer
        @apiGroup Customer

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Customer Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        try:
            artisend_user = ArtisendUser.objects.get(user=request.auth.user)
            artisend_user.user.last_name = request.data["last_name"]
            artisend_user.user.email = request.data["email"]
            artisend_user.address = request.data["address"]
            artisend_user.phone_number = request.data["phone_number"]
            artisend_user.user.save()
            artisend_user.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return HttpResponseServerError(str(e))