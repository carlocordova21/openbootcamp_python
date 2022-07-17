class Alumno:
   def __init__(self, nombre, nota):
      self.nombre = nombre
      self.nota = nota

   def __str__(self):
      return ("nombre={}, nota={}".format(self.nombre, self.nota))

   def es_aprobado(self):
      if self.nota >= 5:
         print("El alumno {} esta aprobado".format(self.nombre))
      else:
         print("El alumno {} esta desaprobado".format(self.nombre))
   
alumno = Alumno("Juan", 15)
alumno.es_aprobado()
