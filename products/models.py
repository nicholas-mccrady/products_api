from unicodedata import decimal
from django.db import models
from io import BytesIO
from urllib.request import urlopen
from django.core.files import File


# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quantity = models.IntegerField()
    product_image = models.TextField(max_length=10000, default='')
