from django.urls import path , include
from rest_framework import routers
from .views  import *


# Crea una instancia del router
router = routers.DefaultRouter()
router.register(r'pots', postViewSet),
router.register(r'citas', CitasViewSet)





# Define las rutas
urlpatterns = [
    path ('', include(router.urls))
]




