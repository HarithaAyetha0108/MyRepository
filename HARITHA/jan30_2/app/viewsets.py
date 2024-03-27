from rest_framework import viewsets
from django.contrib.auth.models import User
from app.models import Role,UserProfile
from app.serializers import RoleSerializer,UserProfileSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

class RoleViewSet(viewsets.ModelViewSet):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
        
    def perform_create(self,serializer):
        data=serializer.data 
        role_id=data.pop("role")
        user1=User.objects.create_user(**data)
        print(user1,'hhhhhhhhhhh'*20)
        role_instance=Role.objects.get(id=role_id)
    #     # UserProfile(user=user1,role=role_instance).save()
   

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
             