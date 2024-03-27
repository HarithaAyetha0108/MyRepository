from django.db import models
from django.contrib.auth.models import User


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     pancard = models.CharField(max_length=100)
#     aadharcard=models.CharField(max_length=100)


class UserProfile(User):
    pancard=models.CharField(max_length=100)
    aadharcard=models.CharField(max_length=100)

    