from app.viewsets import PersonModelViewset
from rest_framework.routers import DefaultRouter
from app.views import *
from django.urls import path
router = DefaultRouter()
router.register(r'viewset_person', PersonModelViewset, basename='viewset_person')


urlpatterns = [
    path("login",Login.as_view())
    # path("person/<int:pk>/", SampleView.as_view()),
    # path("person/", SampleView.as_view())

    # path("viewset_person/", PersonViewset.as_view({"post": "post_method"}))
    # path("viewset_person/<int:pk>", PersonViewset.as_view({"put": "put_method",
    #                                                   "delete": "delete_method"}))
    
    
] + router.urls

