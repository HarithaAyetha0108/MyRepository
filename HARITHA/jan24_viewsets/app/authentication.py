from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import exceptions
import jwt
# class MyAuthentication(BaseAuthentication):
#     def authenticate(self, request):
        
#         return super().authenticate(request)

class JWTAuth(TokenAuthentication):
   def authenticate_credentials(self, key):
        try:
            payload=jwt.decode(key, 'secret', algorithms="HS256")
            user_inst=User.objects.get(pk=payload.get("userId"))
        except Exception as err:
            raise exceptions.AuthenticationFailed("Invalid token99999")
        if not user_inst.is_active:
            raise exceptions.AuthenticationFailed("User inactive or deleted")
        return (user_inst,key)
   