from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_impares = list(filter(lambda x: x % 2 != 0, lista))
print(lista_impares)
suma_impares = reduce(lambda x, y: x + y, lista_impares)
print(suma_impares)