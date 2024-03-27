from django.db import models
from django.contrib.auth.models import AbstractUser



class BaseAbstractionModel(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        abstract=True 

class Role(BaseAbstractionModel):
    pass

class MyUser(AbstractUser):
    role=models.ForeignKey(Role, on_delete=models.PROTECT)

