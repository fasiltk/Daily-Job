from django.urls import path
from .views import *
urlpatterns = [
    path("home/",home,name='home'),
    path("approve/<id>",approve,name='delete_booking'),
    path("delete/<id>",delete,name='delete_booking'),
    
    ]