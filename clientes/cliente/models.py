from django.db import models

# Create your models here.
class Clientes(models.Model):
    name_client = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    user_created = models.ForeignKey(max_length=100)
    is_active = models.BooleanField(max_length=100)


    def __str__(self) :
        return self.name_client