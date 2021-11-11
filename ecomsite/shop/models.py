from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=120)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postalcode = models.CharField(max_length=200)


