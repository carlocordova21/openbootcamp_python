peso = float(input("Ingrese peso en kg: "))
estatura = float(input("Ingrese estatura en metros: "))

imc = peso / (estatura ** 2)
imc = round(imc, 2)
print("IMC: ", imc)