from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static

from principal.views import *


# Crea una instancia del router
router = routers.DefaultRouter()
router.register(r'pots', PostViewSet, basename='Post'),
router.register(r'citas', CitasViewSet, basename='Citas')
router.register(r'taller', TallerViewSet, basename='Taller')
router.register(r'usuario', UsuarioViewSet, basename='Usuario')
router.register(r'municipio', MunicipioViewSet, basename='Municipio')
router.register(r'documento', TdocumentoViewSet, basename='Tdocumento')
router.register(r'Comentarios', ComentariosViewSet, basename='Comentarios')








# Define las rutas
urlpatterns = [
    path('', include(router.urls)),
    path('login/',CreateTokenView.as_view()),
]
