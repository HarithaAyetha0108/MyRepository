from django.shortcuts import render
from rest_framework.views import APIView
from app.serializers import *
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count,Sum,Min

# Create your views here.
class VisitorView(APIView):
    def post(self,request):
        data={}
        ser=VisitorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            status_code=status.HTTP_200_OK
            data=ser.data
        else:
            status_code=ser.errors 
        
        return Response({"result":data},status_code)

    # def get(self,request):
    #     vis=Visit.objects.all()
    #     seri=VisitorSerializer(vis,many=True)
    #     visits = Visit.objects.annotate(     total_visits=Count('id'),     
    #     resources_used=Count(case(resources__icontains=='CPU', then=Value('CPU')),             
    #             (resources__icontains='DESKTOP', then=Value('DESKTOP')),          
    #             (resources__icontains='MONITOR', then=Value('MONITOR')),            
    #             (resources__icontains='KEYBOARD', then=Value('Keyboard')),     
    #     data=resources_used.data
    #     return Response({"result":data}) 

    # def get(self, request):
    #     # Aggregate data using Django ORM
    #     visits_data = Visit.objects.annotate(
    #         total_visits=Count('id'),
    #         resources_used=Count(
    #             Case(
    #                 When(resources__icontains='CPU', then=Value(1)),
    #                 When(resources__icontains='DESKTOP', then=Value(1)),
    #                 When(resources__icontains='MONITOR', then=Value(1)),
    #                 When(resources__icontains='KEYBOARD', then=Value(1)),
    #                 default=Value(0),
    #                 output_field=CharField()
    #             )
    #         )
    #     )

    #     # Serialize the data
    #     serializer = VisitorSerializer(visits_data, many=True)

    #     # Return the response
    # #     return Response({"resultkkkkk": serializer.data})
    # def get(self, request):
    #     # aggregated_data = Visit.objects.annotate(
    #     # total_visits=Count('name'),
    #     # most_visited_floor=Count('floor', distinct=True),
    #     # resources_used= Concat('resources', Value(','), output_field=CharField()))
    #     # serializer = VisitorSerializer(aggregated_data, many=True)

        

    #     return Response({"resultkkkkk": serializer.data})



    def get(self,request):
        queryset=Visit.objects.all()
        result = queryset.values('name').annotate(
            total_visits=Count('floor'),
            resources_used=Count('resources'))
        
        print(result)
        for item in result:
            resources = set(Visit.objects.filter(name=item['name']).values_list('resources', flat=True))
            print(resources)
            item['resources_used'] = ', '.join(resources)
            print(item)
        

        # # Group by 'name' again to find the most visited floor for each person
        most_visited_floors = queryset.values('name').annotate(most_visited_floor=Min('floor'))

        # # Merge the two result sets
        print(most_visited_floors,"Fffffffffff")
        print(result,"KKKKKKKK")
        for item in result:
            most_visited_floor = next(filter(lambda x: x['name'] == item['name'], most_visited_floors),
                                         {}).get('most_visited_floor')
            print(most_visited_floor,"jjjjjjjj")
            item['most_visited_floor'] = most_visited_floor
            print(item,"iiiiiiiiiiii")
    
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
