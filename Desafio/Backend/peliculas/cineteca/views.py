from rest_framework import viewsets
from .models import Movie
from .serializers import PeliculaSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = PeliculaSerializer
