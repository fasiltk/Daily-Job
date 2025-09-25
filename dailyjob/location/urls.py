from django.urls import path
from .views import *

urlpatterns = [

    path('map_view/',map_view,name='map_view'),

]