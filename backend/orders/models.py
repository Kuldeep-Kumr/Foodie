from django.db import models
from restaurant.models import Restaurant,Menu
from users.models import User

class Order(models.Model):
    ORDER_STATUS=(
        ('placed','Placed'),
        ('preparing','Preparing'),
        ('ready','Ready'),
        ('delivered','Delivered')
    )
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0.0)
    date = models.DateTimeField(("Date"),auto_now=True)
    status=models.CharField(("Order Status"),max_length=50,choices=ORDER_STATUS)
