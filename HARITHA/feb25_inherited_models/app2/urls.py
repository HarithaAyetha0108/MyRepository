from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app2.viewsets import UserProxyProfileViewSet

router = DefaultRouter()
router.register(r'userproxyprofiles', UserProxyProfileViewSet, basename='user-profile')

urlpatterns = [
    # path('', include(router.urls)),
] +router.urls


