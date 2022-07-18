from requests import patch


path = "ejercicio10/ejemplo.txt"
file = open(path, "w")
file.close()

file = open(path, "w")
file.write("Hola mundo")
file.close()