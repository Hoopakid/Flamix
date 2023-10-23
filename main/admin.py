from django.contrib import admin

from .models import ShoppingCart, Image, Products

# Register your models here.

admin.site.register((ShoppingCart, Image, Products))
