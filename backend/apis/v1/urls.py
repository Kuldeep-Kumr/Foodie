from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Code Block
app_name = "v1_apis"

router = DefaultRouter()



urlpatterns = [
    path("api/v1/", include([
        path("user/", include("users.api.v1.urls")),
        path("user/", include("reviews.api.v1.urls")),
        path("restaurant/", include("restaurant.api.v1.urls")),
        path("", include("orders.api.v1.urls"))]
    ))]
    
