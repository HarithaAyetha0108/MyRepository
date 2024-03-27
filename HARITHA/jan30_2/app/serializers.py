from rest_framework import serializers
from app.models import Role,UserProfile
from django.contrib.auth.models import User

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=["name"]

class UserProfileSerializer(serializers.ModelSerializer):
    role=serializers.IntegerField()
    class Meta:
        model=User
        fields=["username","password","email","role"]

