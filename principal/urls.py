from django.urls import path , include
from rest_framework import routers
from .views  import *


<<<<<<< HEAD
# routers= routers.DefaultRouter()
# routers.register(r'usuario',usuarioViewSet)


urlpatterns = [
    # path('',include(routers.urls))
    path('usuario',usuarioViewSet.as_view()),
    path('', include(router.urls)),
=======
routers= routers.DefaultRouter()
routers.register(r'pots',postViewSet)


urlpatterns = [
    path('',include(routers.urls))

>>>>>>> 5cf31727af9f3b7ca36536f4856693b348b5ab3c
]
