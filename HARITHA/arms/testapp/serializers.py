from rest_framework import serializers 
from testapp.models import *
from django.core.exceptions import ValidationError

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)

# class ProductSerializer(serializers.Serializer):
#     cost = serializers.DecimalField(max_digits=10, decimal_places=2)
#     openingstock = serializers.DecimalField(max_digits=10, decimal_places=2)
#     name = serializers.CharField(max_length=250)
#     category = serializers.IntegerField()
#     product_unque_number = serializers.IntegerField()
    
class ProductModelSerializer(serializers.ModelSerializer):
    # cost = # that should directly reffer the models.ProductCost.cost#serializers.DecimalField(max_digits=10, decimal_places=2)
    # openingstock =#that should directly reffer the models.Openingstock.stock #serializers.DecimalField(max_digits=10, decimal_places=2)
    cost = serializers.DecimalField(source="productcost.cost",max_digits=10, decimal_places=2)
    openingstock =serializers.DecimalField(source="openingstock.stock",max_digits=10, decimal_places=2)
    class Meta:
        model = Product
        fields = ("name", "product_unique_number", "category",
                  "cost","openingstock")


# for get method in productview
class ProductModellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductPurchaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPurchase
        fields = '__all__'

class ProductSalesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductSales
        fields='__all__'        
    
class StockReportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=StockReport
        fields='__all__'
        # fields=("name", "category","product_unique_number","product",
                # "openingstock","quantity_p","quantity_s","quantity_onhand")





class PurchaseOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields='__all__'
    
class SalesOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesOrder
        fields='__all__'
        