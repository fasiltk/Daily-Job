from django.urls import path
from .views import *

app_name = "location"


urlpatterns = [
    path('map_view/',map_view,name='map_view'),
]