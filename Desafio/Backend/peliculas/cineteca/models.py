from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(max_length=200)
    rating = models.IntegerField()
    genres = models.TextField()
    def __str__(self):
        return self.name
