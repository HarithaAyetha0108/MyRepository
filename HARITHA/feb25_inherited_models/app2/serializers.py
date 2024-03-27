from rest_framework import serializers
from app2.models import *

class ProxyUserProfileSerializer(serializers.ModelSerializer):
    pancard=serializers.SerializerMethodField()
    class Meta:
        model=ProxyUserProfile
        fields="__all__"

    def get_pancard(self,obj):
        return obj.check_pancard()
    
    