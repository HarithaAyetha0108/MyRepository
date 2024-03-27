# from django.contrib import admin
# from django.urls import path 
# from app.viewsets import RoleViewSet, MyUserViewSet
# from rest_framework.routers import  DefaultRouter 
# router=DefaultRouter() 
# router.register(r'role',RoleViewSet,basename="role")
# router.register(r'user',MyUserViewSet,basename="user")

# url_patterns = [
    

# ]  +router.urls

from django.contrib import admin
from app.viewsets import MyUserViewSet,RoleViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', MyUserViewSet, basename="user")
router.register(r'role', RoleViewSet, basename="role")
urlpatterns = [
    
] + router.urls
