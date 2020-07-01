from django.contrib import admin
from order.models import Product, Order, OrderItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
