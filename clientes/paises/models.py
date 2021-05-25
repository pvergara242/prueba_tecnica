from django.db import models

# Create your models here.
class Paises(models.Model):
    name = models.CharField(max_length=100)