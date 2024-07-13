from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    genres = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name
