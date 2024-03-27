from rest_framework import viewsets
from django.contrib.auth.models import User
from app1.models import UserProfile
from app1.serializers import UserProfileSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
