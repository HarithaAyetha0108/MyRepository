from django.urls import path 
from app.viewsets import RoleViewSet,UserProfileViewSet
from rest_framework.routers import DefaultRouter 
router=DefaultRouter()
router.register(r'role', RoleViewSet, basename="role")
router.register(r'user',UserProfileViewSet, basename="user")

urlpatterns = [
    
] + router.urls