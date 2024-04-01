from rest_framework import serializers
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Review
        fields = ('__all__')
    
    def create(self, validated_data):
        return Review.objects.create(**validated_data)
    
class UserReviewSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source="user.username")
    name=serializers.ReadOnlyField(source="user.name")
    dish_name = serializers.ReadOnlyField(source="menu.name")
    dish_img = serializers.ReadOnlyField(source="menu.img_url")
    restaurant_name = serializers.ReadOnlyField(source="restaurant.name")
    
    class Meta:  
        model = Review
        fields = ['id','username','name','restaurant_name','dish_img','dish_name','rating','text','date']