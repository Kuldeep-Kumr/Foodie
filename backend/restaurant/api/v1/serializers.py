from rest_framework import serializers
from restaurant.models import Restaurant,Menu

class MenuSerializer(serializers.ModelSerializer):
    avg_rating = serializers.DecimalField(max_digits=3,decimal_places=1,read_only=True)
    class Meta:  
        model = Menu
        fields = ['id','restaurant','img_url','name','price','description','avg_rating']

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)
    

class RestaurantSerializer(serializers.ModelSerializer):
    avg_rating = serializers.DecimalField(max_digits=3,decimal_places=1,read_only=True)
    class Meta:  
        model = Restaurant
        fields = ['id','img_url','name','location','cuisine','avg_rating','user']

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)
