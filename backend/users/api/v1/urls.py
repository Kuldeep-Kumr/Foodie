from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.api.v1.viewsets import UserViewSet,CustomAuthToken

# Code Block

app_name = "user_api_v1"

router = DefaultRouter()
router.register(r"auth", UserViewSet, basename="user_auth")

# Url Paterns
urlpatterns = [
    path("auth/login/",CustomAuthToken.as_view()),
    path("", include(router.urls)),
]