from rest_framework.routers import DefaultRouter
from .viewsets import RestaurantViewSet,RestaurantMenuViewSet,OrderViewSet
# Code Block

app_name = "restaurant_api_v1"

router = DefaultRouter()
router.register(r"", RestaurantViewSet, basename="resturant")

router.register(r"owner/menu", RestaurantMenuViewSet, basename="resturant-menu")
router.register(r"owner/order",OrderViewSet,basename="resturant-order")
# Url Paterns
urlpatterns = router.urls