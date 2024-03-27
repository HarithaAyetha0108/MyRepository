from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import UserProfile,Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role    
        fields=["name"]

class UserRegistrationSerializer(serializers.ModelSerializer):
    role=serializers.IntegerField()
    class Meta:
        model = User
        fields = ["username","password","email","role"]

        