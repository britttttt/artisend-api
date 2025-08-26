import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from artisendapi.models import UserProfile
from artisendapi.utils.geolocation import geocode_postal_code
from django.contrib.auth import authenticate


@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        req_body = json.loads(request.body.decode())
        username = req_body.get("username")
        password = req_body.get("password")
    except (json.JSONDecodeError, KeyError):
        return JsonResponse(
            {"valid": False, "error": "Invalid JSON or missing fields"}, status=400
        )

    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({"valid": True, "token": token.key, "id": user.id})

    return JsonResponse({"valid": False}, status=401)


@csrf_exempt
def register_user(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        postal_code = request.POST.get('postal_code', '')
        avatar = request.FILES.get('avatar')  # File upload

        if not username or not password or not email:
            return JsonResponse({"error": "Missing required fields"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        new_user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        profile = new_user.userprofile
        profile.postal_code = postal_code
        profile.latitude, profile.longitude = geocode_postal_code(postal_code)
        if avatar:
            profile.profile_pic = avatar
        profile.save()

        token = Token.objects.create(user=new_user)
        return JsonResponse({"token": token.key, "id": new_user.id}, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)