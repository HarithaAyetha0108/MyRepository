from rest_framework import serializers
from django.contrib.auth.models import User
from app1.models import UserProfile

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password','email')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

    # def create(self, validated_data):
    #     print(validated_data)
    #     user_data = validated_data.pop('user')
    #     print(user_data)
    #     user = User.objects.create(**user_data)
    #     print(user)
    #     profile = UserProfile.objects.create(user=user, **validated_data)
    #     print(profile)
    #     return profile



