from rest_framework import viewsets
from app.models import *
from app.serializers import *

class SampleViewSet(viewsets.ModelViewSet):
    queryset=Sample.objects.all()
    serializer_class=SampleSer
