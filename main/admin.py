from django.contrib import admin

from .models import ShoppingCart, Image, Products, Comment, ComboProducts, ShoppingCartCombo, Blogs

# Register your models here.

admin.site.register((Image, Products, ComboProducts, Blogs))
