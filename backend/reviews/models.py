from django.db import models
from restaurant.models import Restaurant,Menu
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    text = models.CharField(("Review Text"),max_length=256)
    date = models.DateTimeField(("Review Date"),auto_now=True)