from django.contrib import admin
from users.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','name','phone','is_owner','password')

    search_fields = ("username","name","is_owner",)
