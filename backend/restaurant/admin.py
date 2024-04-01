from django.contrib import admin
from restaurant.models import Restaurant,Menu
from django.utils.html import format_html

# Register your models here.

@admin.register(Restaurant)
class ResturantAdmin(admin.ModelAdmin):
    def image(self,obj):
        return format_html('<img src="{}" style="max-width:80px; max-height:80px"/>'.format(obj.img_url))

    list_display = ('user','image','name','location','cuisine')
    image.short_description = 'Image'

    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    def image(self,obj):
        return format_html('<img src="{}" style="max-width:80px; max-height:80px"/>'.format(obj.img_url))

    list_display = ('restaurant','image','name','price','description')
    image.short_description = 'Image'
    
