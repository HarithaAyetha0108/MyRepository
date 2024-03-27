from app.models import Person
from rest_framework import serializers

class PersonSer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'
        