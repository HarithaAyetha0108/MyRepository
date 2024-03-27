from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250)
    age = models.IntegerField(default=0)
    created_by_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="created_name")
    updated_by_id=models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="update_name")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=30,default="Active")
