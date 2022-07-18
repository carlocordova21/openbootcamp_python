class Vehiculo:
   def __init__(self, marca, modelo):
      self.marca = marca
      self.modelo = modelo

   def acelerar(self):
      print("Acelerando")

   def frenar(self):
      print("Frenando")

import pickle
vehiculo = Vehiculo("Ford", "Mustang")

path = "ejercicio11/datos.bin"
fichero = open(path, "wb")
pickle.dump(vehiculo, fichero)
fichero.close()

f = open(path, "rb")
fichero_load = pickle.load(f)
f.close()

print(type(fichero_load))
print(fichero_load.marca)
print(fichero_load.modelo)