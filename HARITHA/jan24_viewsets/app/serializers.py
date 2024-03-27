from rest_framework import serializers 
from app.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def create(self,validated_data):
        request=self.context.get('request')
        instance=self.Meta.model(**validated_data)
        instance.created_by_id=request.user
        instance.save()
        return instance 


    def update(self,instance,validated_data):
        request=self.context.get('request')
        instance.name=validated_data.get("name",instance.name) ##already saved name,postman name
        instance.email=validated_data.get("email",instance.email)
        instance.age=validated_data.get("age",instance.age)
        instance.updated_by_id= request.user
        instance.save()
        return instance 


