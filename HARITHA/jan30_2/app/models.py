from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    name=models.CharField(max_length=100)

class UserProfile(models.Model):
    username=models.OneToOneField(User, on_delete=models.PROTECT)
    role=models.ForeignKey(Role,on_delete=models.PROTECT)