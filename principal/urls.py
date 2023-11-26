from django.urls import path , include
from rest_framework import routers
from .views  import *


routers= routers.DefaultRouter()
routers.register(r'pots',postViewSet)


urlpatterns = [
    path('',include(routers.urls))

]
