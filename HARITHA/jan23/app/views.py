from django.shortcuts import render
from app.serializers import PersonSer
from app.models import Person
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response


# Create your views here.

class PersonView(APIView):
    # login_api = ' http://127.0.0.1:8006/login'
    def post(self,request):
        data={}
        ser=PersonSer(data=request.data)
        if ser.is_valid():
            ser.save()
            message="ok"
            status_code= status.HTTP_200_OK
            data=ser.data 
        else:
            message=ser.errors
            status_code=status.HTTP_400_BAD_REQUEST 
        return Response({"result":message,"data":data}, status=status_code)
    
    def get(self,request):
        persons=Person.objects.all()
        ser=PersonSer(persons,many=True)
        data=ser.data 
        return Response(data)
    

                
