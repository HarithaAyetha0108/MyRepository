from django.db import models

# Create your models here.
class Visit(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    floor=models.IntegerField()
    resources=models.CharField(max_length=100)