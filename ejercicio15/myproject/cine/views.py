from django.shortcuts import render
from .models import Peliculas, Directores

def index(request):
   peliculas = Peliculas.objects.all()
   directores = Directores.objects.all()
   num_directores = Directores.objects.all().count()
   num_peliculas = Peliculas.objects.all().count()
   return render(
      request, 
      'index.html',
      context={
         'num_directores': num_directores,
         'num_peliculas': num_peliculas,
         'peliculas': peliculas,
         'directores': directores
      }
   )