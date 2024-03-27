from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import jwt
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Login(APIView):
    authentication_classes = []
    permission_classes = []
    import pdb;pdb.set_trace()
    def post(self,request):
        data = request.data
        resp_data = {"token":None,"message":""}
        user = authenticate(username = data['username'],password = data['password'])
        if user:
            payload = {"userName":user.username,"userId" : user.id}
            # payload={"user":user}
            resp_data["token"] = jwt.encode(payload,"secret",algorithm="HS256")
            resp_data["message"] = "ok"
            return Response(resp_data)
        else:
            return Response(resp_data,status= status.HTTP_403_FORBIDDEN)