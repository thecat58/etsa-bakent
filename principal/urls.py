from django.urls import path , include
from rest_framework import routers
from principal.views import *

routers= routers.DefaultRouter()
routers.register(r'post',PostioViewSet)


urlpatterns = [
    path('',include(routers.urls))

]
