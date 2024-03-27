from django.contrib import admin
from django.urls import path
from testapp.views import *

urlpatterns = [
    path("login",Login.as_view()),
    path("category/", CategoryView.as_view()),
    path("product/", ProductView.as_view()),
    path("productpurchase/", ProductPurchaseView.as_view()),
    path("productsales/", ProductSalesView.as_view()),
    # path("purchaseorder/", PurchaseOrderView.as_view()),
    # path("salesorder/",SalesOrderView.as_view()),
    path("stockreport/",StockReportAllView.as_view()),
    path("stockreport/<int:id>",StockReportView.as_view())
]






# product
# {
#     "name":"realme",
#     "product_unique_number":"14",
#     "category":1,
#     "cost":43000,
#     "openingstock":10
# }



# productpurshase
# [
#     {"product": 1, "quantity_s": 15},
#     {"product": 2, "quantity_s": 20}
# ]

# productsale
# [
#     {"product": 1, "quantity_p": 15},
#     {"product": 2, "quantity_p": 20}
# ]

