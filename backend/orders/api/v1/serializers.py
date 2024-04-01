from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Order
        fields = ('__all__')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
    def update(self, instance, validated_data):  
        instance.status= validated_data.get('status', instance.status)    
        instance.save()  
        return instance

class UserOrderSerializer(serializers.ModelSerializer):
    email=serializers.ReadOnlyField(source="user.username")
    name=serializers.ReadOnlyField(source="user.name")
    dish_name = serializers.ReadOnlyField(source="menu.name")
    dish_img = serializers.ReadOnlyField(source="menu.img_url")
    restaurant_name = serializers.ReadOnlyField(source="restaurant.name")

    class Meta:  
        model = Order
        fields = ['id','email','name','restaurant_name','dish_img','dish_name','status','quantity','price','date']


