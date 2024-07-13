#from django.shortcuts import render
from rest_framework import viewsets
from .models import Pelicula
from .serializers import PeliculaSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
