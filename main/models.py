from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Products(models.Model):
    title = models.CharField(max_length=150)
    cost = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(upload_to='pics')
    service = models.ForeignKey(Products, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    service = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.service.title} from {self.user.username}'
