from django.db import models

# Create your models here.
from django.db import models

class Localizacao(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cidade}, {self.estado} - {self.pais}"
