from django.db import models
# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    pokemon_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name