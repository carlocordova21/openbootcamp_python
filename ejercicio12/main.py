from traceback import print_tb


cantidad = int(input("Ingrese cantidad de paises: "))
lista_paises = []
for i in range(cantidad):
   pais = input(f"Ingrese {i+1}° nombre del pais: ")
   lista_paises.append(pais)

conjunto = set(lista_paises)
conjunto_ordenado = sorted(conjunto)

resultado = ", ".join(conjunto_ordenado)
print(resultado)