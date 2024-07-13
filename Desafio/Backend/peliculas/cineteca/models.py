from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    description = models.TextField()
    genres = models.CharField(max_length=200)  # Puedes almacenar los géneros como una cadena separada por comas
    rating = models.IntegerField()

    def __str__(self):
        return self.name