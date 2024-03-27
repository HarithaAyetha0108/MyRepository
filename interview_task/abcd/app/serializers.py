from rest_framework import serializers
from app.models import *

class SampleSer(serializers.ModelSerializer):
    # sum=serializers.IntegerField(read_only=True)   
    sum=serializers.SerializerMethodField()  
    # print(type(sum))        ###type=<class 'rest_framework.fields.SerializerMethodField'>
    class Meta:
        model=Sample
        fields=["a","b","c","sum"]

    # def get_sum(self,obj):
    #     return obj.a+obj.b+obj.c

    def get_sum(self,obj):
        return obj.summ   ##we have to give method name which is present in models(we can use @property method or generator field or directly give in serializer)
    