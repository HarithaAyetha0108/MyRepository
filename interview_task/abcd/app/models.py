from django.db import models

# Create your models here.

class Sample(models.Model):
    a=models.IntegerField()
    b=models.IntegerField()
    c=models.IntegerField()



    @property
    def summ(self):
        return self.a+self.b+self.c
    
    