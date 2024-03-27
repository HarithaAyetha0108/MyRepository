from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer,RoleSerializer
from django.contrib.auth.models import User
from app.models import Role,UserProfile

class RoleViewSet(viewsets.ModelViewSet):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        data = serializer.data
        role_id = data.pop("role")
        user1 = User.objects.create_user(**data)
        role_inst = Role.objects.get(id=role_id)
        UserProfile(user=user1, role=role_inst).save()
        
        



    