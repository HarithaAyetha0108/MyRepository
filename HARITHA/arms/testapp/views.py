from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.models import *
from testapp.serializers import *
from rest_framework import status
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
import jwt
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
class Login(APIView):
   
   
    def post(self,request):
        data = request.data
        resp_data = {"token":None,"message":""}
        user = authenticate(username = data['username'],password = data['password'])
        if user:
            #import pdb;pdb.set_trace()
            payload = {"userName":user.username,"userId" : user.id}
            # payload={"user":user}
            # resp_data["token"]="@@@@@@"
           
            resp_data["token"] = jwt.encode(payload,"secret",algorithm="HS256")
            resp_data["message"] = "ok"
            return Response(resp_data)
        else:
            return Response(resp_data,status= status.HTTP_403_FORBIDDEN)
        
# class Login(APIView):
#     def post(self,request):
#         data=request.data
#         res={"token":None,"message":""}
#         user=authenticate(**data)
#         if user:
#              token_inst=Token.objects.filter(user=user)
#              if not token_inst.exists():
#                  token_inst=Token.objects.create(user=user)
#              else:
#                  token_inst=token_inst[0]    
#              res["token"]=token_inst.key 
#              res["message"]="ok"
#              return Response(res)        
#         return Response(res,status=status.HTTP_403_FORBIDDEN)
                 

class CategoryView(APIView):
    def post(self, request):
        data = {}
        ser = CategoryModelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            message = "inserted successfully"
            status_code = status.HTTP_201_CREATED
            data = ser.data
        else:
            message=ser.errors
            status_code = status.HTTP_400_BAD_REQUEST

        return Response({"Result":message,"data": data}, status=status_code)
    
    def get(self,request):
        products=Category.objects.all()
        ser=CategoryModelSerializer(products,many=True)
        data=ser.data 
        return Response(data)


class ProductView(APIView):
    def post(self, request):
        data = {}
        ser = ProductModelSerializer(data=request.data)
        #ser.instance # model instanc
        # product_model_instance.category.name
        if ser.is_valid():
            a=ser.save()
            cost_data=request.data.get('cost')
            a.productcost_set.create(cost=cost_data)
            opening_stock=request.data.get('openingstock')
            a.openingstock_set.create(stock=opening_stock)
            message = "inserted successfully"
            status_code = status.HTTP_201_CREATED
            data = ser.data
        else:
            message=ser.errors
            status_code = status.HTTP_400_BAD_REQUEST

        return Response({"Result":message,"data": data}, status=status_code)


    def get(self,request):
        products=Product.objects.all()
        ser=ProductModellSerializer(products,many=True)
        data=ser.data 
        return Response(data)

class ProductPurchaseView(APIView):
    def post(self, request):
        if isinstance(request.data, list):
            serializer = ProductPurchaseModelSerializer(data=request.data, many=True)
        else:
            serializer = ProductPurchaseModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        products_purchase=ProductPurchase.objects.all()
        ser=ProductPurchaseModelSerializer(products_purchase,many=True)
        data=ser.data 
        return Response(data)

class ProductSalesView(APIView):
    def post(self, request):
      if isinstance(request.data, list):
            serializer = ProductSalesModelSerializer(data=request.data, many=True)
      else:
            serializer = ProductSalesModelSerializer(data=request.data)

      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

    def get(self,request):
        products_purchase=ProductSales.objects.all()
        ser=ProductSalesModelSerializer(products_purchase,many=True)
        data=ser.data 
        return Response(data)
    

class StockReportView(APIView):
    def get(self, request, id, *args, **kwargs):
        product = Product.objects.get(id=id)
        opening_stock = OpeningStock.objects.filter(product_id=id).aggregate(total_stock=Sum('stock'))['total_stock'] or 0
        total_purchase_stock = ProductPurchase.objects.filter(product_id=id).aggregate(total_stock=Sum('quantity_p'))['total_stock'] or 0
        total_sale_stock = ProductSales.objects.filter(product_id=id).aggregate(total_stock=Sum('quantity_s'))['total_stock'] or 0
        category_serializer = CategoryModelSerializer(product.category)
        response_data = {
            'product_id': product.id,
            'product_name': product.name,
            'product_category': category_serializer.data["name"],
            'product_unique_num': product.product_unique_number,
            'opening_stock': opening_stock,
            'no_of_quantity_purchase': total_purchase_stock,
            'no_of_quantity_sale': total_sale_stock,
            'quantity_onhand': (opening_stock + total_purchase_stock - total_sale_stock)
        }

        return Response(response_data, status=status.HTTP_200_OK)


class StockReportAllView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        response_data_list = []
        for product in products:
            opening_stock = OpeningStock.objects.filter(product_id=product.id).aggregate(total_stock=Sum('stock'))['total_stock'] or 0
            total_purchase_stock = ProductPurchase.objects.filter(product_id=product.id).aggregate(total_stock=Sum('quantity_p'))['total_stock'] or 0
            total_sale_stock = ProductSales.objects.filter(product_id=product.id).aggregate(total_stock=Sum('quantity_s'))['total_stock'] or 0
            category_serializer = CategoryModelSerializer(product.category)
            
            # Create response data for each product
            product_data = {
                'product_id': product.id,
                'product_name': product.name,
                'product_category': category_serializer.data["name"],
                'product_unique_num': product.product_unique_number,
                'opening_stock': opening_stock,
                'no_of_quantity_purchase': total_purchase_stock,
                'no_of_quantity_sale': total_sale_stock,
                'quantity_onhand': (opening_stock + total_purchase_stock - total_sale_stock)
            }

            # Append the product data to the response data list
            response_data_list.append(product_data)

        # Return the response data list
        return Response(response_data_list, status=status.HTTP_200_OK)




class PurchaseOrderView(APIView):
    def post(self, request):
       print(request.data, )
       data={}
       ser=PurchaseOrderModelSerializer(data=request.data)
       if ser.is_valid():
           ser.save()
           message="inserted successfully"
           data=ser.data 
       else:
           message=ser.errors 
        
       return Response({"Result":message,"data":data})        

    def get(self,request):
        purchases=PurchaseOrder.objects.all()
        ser=PurchaseOrderModelSerializer(purchases,many=True)
        data=ser.data 
        return Response(data)

class SalesOrderView(APIView):
    def post(self, request):
       data={}
       ser=SalesOrderModelSerializer(data=request.data)
       if ser.is_valid():
           ser.save()
           message="inserted successfully"
           data=ser.data 
       else:
           message=ser.errors 
        
       return Response({"Result":message,"data":data})        

    def get(self,request):
        sales=SalesOrder.objects.all()
        ser=SalesOrderModelSerializer(sales,many=True)
        data=ser.data 
        return Response(data)

# class LoginAPI(APIView):
#     def post(self,request):
#         username=request.data.get('username')
#         password=request.data.get('password')
#         user=authenticate(user)