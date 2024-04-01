from rest_framework.authtoken.models import Token
from restaurant.api.v1.serializers import RestaurantSerializer
from restaurant.models import Restaurant

def get_user_id(request):
    auth_header = request.META['HTTP_AUTHORIZATION']
    token = auth_header.split()[1]
    token_obj = Token.objects.get(key=token)
    user = token_obj.user
    return user.id

def get_restaurant_id(request):
    auth_header = request.META['HTTP_AUTHORIZATION']
    token = auth_header.split()[1]
    token_obj = Token.objects.get(key=token)
    user = token_obj.user
    store_object=Restaurant.objects.filter(user=user.id)
    serializer=RestaurantSerializer(store_object,many=True)
    try:
        return serializer.data[0]['id']
    except:
        return serializer.error_messages


