from django.urls import path, include
from .views import PeliculaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
