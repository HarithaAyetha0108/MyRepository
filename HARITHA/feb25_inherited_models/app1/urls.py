from django.urls import path, include
from rest_framework.routers import DefaultRouter    
from app1.viewsets import UserProfileViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet, basename='user-profile')

urlpatterns = [
    # path('', include(router.urls)),
] +router.urls


    