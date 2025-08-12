from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from artisendapi.views import register_user, login_user
from artisendapi.views.user_business import UserBusinessViewSet
from artisendapi.views.user_medium import UserMediumViewSet, MediumViewSet
from artisendapi.views.user_skill import UserSkillViewSet, SkillViewSet

# pylint: disable=invalid-name
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'userbusiness', UserBusinessViewSet, basename='userbusiness')
router.register(r'usermedium', UserMediumViewSet, basename='usermedium')
router.register(r'medium', MediumViewSet, basename='medium')
router.register(r'userskill', UserSkillViewSet, basename='userskill')
router.register(r'skill', SkillViewSet, basename='skill')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("api-token-auth", obtain_auth_token),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
