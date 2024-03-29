from django.db import models

class Product(models.Model):
    CHOICE = [('COD', 'Cash ON Delivery'),('ON','Online')]
    product_name = models.CharField(max_length=20)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    delivery_address = models.CharField(max_length=20)
    mode = models.CharField(max_length=20, choices=CHOICE, null=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

