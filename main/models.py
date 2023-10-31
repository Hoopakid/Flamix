from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Products(models.Model):
    title = models.CharField(max_length=150)
    cost = models.IntegerField(default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(upload_to='pics')
    service = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title


class ShoppingCart(models.Model):
    service = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.service.title} from {self.user.username}'


class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ComboProducts(models.Model):
    combo_name = models.CharField(max_length=150)
    product1 = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product1')
    product2 = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product2')
    product3 = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product3')
    product4 = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product4')
    cost = models.IntegerField(default=1)

    def __str__(self):
        return self.combo_name
