from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Person
from app.serializers import PersonSerializer
class PersonViewset(viewsets.ViewSet):
    def post_method(self, request):
        pass

class PersonModelViewset(viewsets.ModelViewSet):
    # import pdb;pdb.set_trace()
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
         data=request.data
         serializer = PersonSerializer(data=data, context={'request': self.request})
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        data=request.data
        pk=kwargs.get('pk',None)
        print(pk)
        ins=Person.objects.get(id=pk)
        ins.status="InActive"
        ins.save()
        return Response({"message":"status field updated succesfully"})
    