from rest_framework import viewsets
from app2.models import *
from app2.serializers import *

class UserProxyProfileViewSet(viewsets.ModelViewSet):
    queryset=ProxyUserProfile.objects.all()
    serializer_class=ProxyUserProfileSerializer


    