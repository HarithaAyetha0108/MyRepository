from app.models import *
from rest_framework import serializers


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visit
        fields="__all__"