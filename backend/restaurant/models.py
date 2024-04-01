from django.db import models
from users.models import User

# Create your models here.

class Restaurant(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img_url = models.URLField(("Restaurant Image"),max_length=256,default='')
    name = models.CharField(("Restaurant Name"),max_length=100,default='')
    location = models.CharField(("Location"),max_length=255,default='')
    cuisine = models.CharField(("Cuisine"),max_length=200,default='')

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    img_url = models.URLField(("Dish image"),max_length=256,default='')
    name = models.CharField(("Dish name"),max_length=100,default='')
    price= models.FloatField(default=0)
    description = models.CharField(("Description"),max_length=500,default='')
    