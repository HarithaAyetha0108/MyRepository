from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("visit/",VisitorView.as_view())
]
