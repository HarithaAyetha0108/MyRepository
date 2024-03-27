from django.contrib import admin
from app.viewsets import UserViewSet,RoleViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'role', RoleViewSet, basename="role")
urlpatterns = [
    
] + router.urls
