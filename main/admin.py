from django.contrib import admin

from .models import ShoppingCart, Image, Products, Comment

# Register your models here.

admin.site.register((ShoppingCart, Image, Products, Comment))
