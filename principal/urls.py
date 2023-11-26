from django.urls import path , include
from rest_framework import routers
from principal.views import *


# routers= routers.DefaultRouter()
# routers.register(r'usuario',usuarioViewSet)


urlpatterns = [
    # path('',include(routers.urls))
    path('usuario',usuarioViewSet.as_view()),
    path('', include(router.urls)),
]
