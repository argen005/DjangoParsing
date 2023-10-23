from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    
class Price(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    site = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

