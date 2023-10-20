from django.contrib import admin

from .models import Service, ShoppingCart, Image, Products

# Register your models here.

admin.site.register((Service, ShoppingCart, Image, Products))
