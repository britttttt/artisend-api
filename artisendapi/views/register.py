import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from artisendapi.models.ArtisendUser import ArtisendUser



@csrf_exempt
def login_user(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        req_body = json.loads(request.body.decode())
        username = req_body.get('username')
        password = req_body.get('password')
    except (json.JSONDecodeError, KeyError):
        return JsonResponse({"valid": False, "error": "Invalid JSON or missing fields"}, status=400)

    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({"valid": True, "token": token.key, "id": user.id})

    return JsonResponse({"valid": False}, status=401)

import requests

def geocode_postal_code(postal_code):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "postalcode": postal_code,
        "countrycodes": "us",  # change as needed
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "artisendapi/1.0 (your_email@example.com)"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200 and response.json():
        result = response.json()[0]
        return float(result["lat"]), float(result["lon"])
    return None, None


@csrf_exempt
def register_user(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        req_body = json.loads(request.body.decode())
        email = req_body['email']
        first_name = req_body.get('first_name', '')
        last_name = req_body.get('last_name', '')
        username = req_body['username']
        password = req_body['password']
        postal_code = req_body.get('postal_code', '') 
    except (json.JSONDecodeError, KeyError):
        return JsonResponse({"error": "Invalid JSON or missing required fields"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username already exists"}, status=400)

    new_user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )

    lat, lng = geocode_postal_code(postal_code)

    artisend_user = ArtisendUser.objects.create(
        user=new_user,
        email=email,
        postal_code=postal_code,
        latitude=lat,
        longitude=lng
    )

    token = Token.objects.create(user=new_user)
    return JsonResponse({"token": token.key, "id": new_user.id}, status=status.HTTP_201_CREATED)