from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r"^\+?1?\d{10,15}$",
    message="Please enter a valid phone number with country code. In the format: '+999999999'.",
)


# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.EmailField(('Email'),max_length=255,unique=True,default='')
    name = models.CharField(('Name'),max_length=100,default='')
    is_owner = models.BooleanField(("Is Owner"),default=False)
    phone = models.CharField(
        ("Phone Number"),
        validators=[phone_validator],
        blank=True,
        null=True,
        max_length=15,
    )
    password=models.CharField(("Password"),max_length=256)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "username"
    REQUIRED_FIELDS = ()