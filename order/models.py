from django.db import models

class Product(models.Model):
    """注文情報"""
    public = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    info = models.TextField()
    like = models.IntegerField(default=0)
    
# Create your models here.
class Order(models.Model):
    """注文情報"""
    status = models.IntegerField()
    name = models.CharField(max_length=255)
    kana = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    subtotal = models.IntegerField(default=0)
    total_tax = models.IntegerField(default=0)
    ship_cost = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    """注文情報"""
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orderitems', on_delete=models.CASCADE)
    status = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    subtotal = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
