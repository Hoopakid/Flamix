from django.contrib import admin

from .models import ShoppingCart, Image, Products, Comment, ComboProducts, ShoppingCartCombo

# Register your models here.

admin.site.register((ShoppingCart, Image, Products, Comment, ComboProducts, ShoppingCartCombo))
