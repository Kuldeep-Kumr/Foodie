from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import ReviewViewSet
# Code Block

app_name = "review_api_v1"

router = DefaultRouter()
router.register(r"review", ReviewViewSet, basename="reviews")
# Url Paterns
urlpatterns = router.urls