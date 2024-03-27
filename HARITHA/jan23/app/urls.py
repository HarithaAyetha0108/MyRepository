from django.contrib import admin
from django.urls import path
from app.views import PersonView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("person/",PersonView.as_view())
]
