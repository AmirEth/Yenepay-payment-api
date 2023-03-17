from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=50)
    merchantId = models.CharField(max_length=100)
    pdtToken = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
