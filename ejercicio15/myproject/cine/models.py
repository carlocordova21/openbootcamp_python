from statistics import mode
from django.db import models
from django.urls import reverse

class Directores(models.Model):
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   nacimiento = models.DateField()

   def __str__(self):
      return self.nombre + " " + self.apellido
   
   def get_absolute_url(self):
      return reverse('cine:director_detail', kwargs={'pk': self.pk})


class Peliculas(models.Model):
   nombre = models.CharField(max_length=50)
   director = models.ForeignKey(Directores, on_delete=models.CASCADE, related_name='peliculas')
   descripcion = models.CharField(max_length=200)
   def __str__(self):
      return self.nombre