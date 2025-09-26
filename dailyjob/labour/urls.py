from django.urls import path
from .views import *

app_name = "labour"


urlpatterns = [
    path("home/",home,name='home'),
    path("approve/<id>",approve,name='delete_booking'),
    path("delete/<id>",delete,name='delete_booking'),
    path("addjob/",addjob,name='addjob'),
    ]