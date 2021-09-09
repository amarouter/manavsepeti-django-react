from django.db import models


# Create your models here.

class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    origin = models.CharField(max_length=100, blank=True, null=True)
    # image =
    price = models.DecimalField(max_digits=7, decimal_places=2)
    count_in_stock = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
