from django.db import models

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=255)
    background_color = models.CharField(max_length=255)
    h1_color = models.CharField(max_length=255)
    p_color = models.CharField(max_length=255)
 
    def __str__(self):
        return self.name