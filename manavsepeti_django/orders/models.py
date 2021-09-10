from django.db import models
from django.contrib.auth.models import User
from ..products.models import Product


# Create your models here.

class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=100)
    tax_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)


class OrderItem(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    qty = models.IntegerField(blank=True, null=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.product.name if self.product.name else self.name
