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
    cost = models.IntegerField(default=1)

    def __str__(self):
        return self.combo_name


class ShoppingCartCombo(models.Model):
    combo_id = models.ForeignKey(ComboProducts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.combo_id.combo_name


class Order(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Wait for payment'),
        (3, 'Paid'),
        (4, 'Delivering'),
        (5, 'Completed')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return f'{self.service.title} >>>> {self.status}'


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    website = models.TextField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name
