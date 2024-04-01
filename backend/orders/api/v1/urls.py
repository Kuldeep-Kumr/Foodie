from rest_framework.routers import DefaultRouter
from .viewsets import OrderViewSet
# Code Block

app_name = "order_api_v1"

router = DefaultRouter()
router.register(r"user/order", OrderViewSet, basename="user_orders")

# Url Paterns
urlpatterns = router.urls