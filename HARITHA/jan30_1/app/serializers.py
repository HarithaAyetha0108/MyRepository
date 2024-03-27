from rest_framework import serializers
from app.models import MyUser,Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=["name"]

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=["username","password","email","role"]        