from django.urls import path 
from app.viewsets import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'sample', SampleViewSet,basename="sample")

urlpatterns=[

] +router.urls