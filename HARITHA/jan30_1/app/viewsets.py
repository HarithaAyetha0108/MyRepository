from rest_framework import viewsets
from app.models import MyUser,Role
from app.serializers import MyUserSerializer,RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer

class MyUserViewSet(viewsets.ModelViewSet):
    queryset=MyUser.objects.all()
    serializer_class=MyUserSerializer
    
    def perform_create(self, serializer):
        data = serializer.data
        role_id=data['role']
        role_instance=Role.objects.get(id=role_id)
        data['role']=role_instance
        MyUser.objects.create_user(**data)   ###create_user means it encrypts the password

