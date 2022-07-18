import time

hora_salida = 18
fecha_actual = time.strftime("%c")
hora_actual = time.strftime("%H:%M:%S")
valor_hora = int(time.strftime("%H"))
print(valor_hora)

if valor_hora > 7:
   print("Son mas de las 7")
else:
   print(hora_salida-valor_hora)