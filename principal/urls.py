from django.urls import path, include
from rest_framework import routers

from principal.views import *


# Crea una instancia del router
router = routers.DefaultRouter()
router.register(r'pots', PostViewSet, basename='Post'),
router.register(r'citas', CitasViewSet, basename='Citas')
router.register(r'taller', TallerViewSet, basename='Taller')





# Define las rutas
urlpatterns = [
    path('', include(router.urls)),
    path('login/',CreateTokenView.as_view()),
    path('citas/',CitasViewSet.as_view),
    # path('usuario/',ususarioViewSet.as_view({'get':'list'})),

]
