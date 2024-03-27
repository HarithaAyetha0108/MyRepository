from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=250)    

class SalesOrder(models.Model):
    description = models.TextField(max_length=250)
    created=models.DateTimeField(auto_now_add=True)

class PurchaseOrder(models.Model):
    description = models.TextField(max_length=250)
    created=models.DateTimeField(auto_now_add=True)    

class Product(models.Model):
    name = models.CharField(max_length=250)
    product_unique_number = models.CharField(max_length=250, unique=True)  
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    # purchase_orders = models.ManyToManyField('PurchaseOrder',through='ProductPurchase',blank=True)
    # sales_orders = models.ManyToManyField('SalesOrder',through='ProductSales',blank=True)

class ProductCost(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

class OpeningStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

class ProductPurchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # purchase_order=models.ForeignKey(PurchaseOrder, on_delete=models.PROTECT)
    quantity_p=models.IntegerField()    

class ProductSales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # sales_order=models.ForeignKey(SalesOrder, on_delete=models.PROTECT)
    quantity_s=models.IntegerField()    

class StockReport(models.Model):
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock_reference_id = models.IntegerField()
    type = models.CharField(max_length=255) 
    stock = models.IntegerField()