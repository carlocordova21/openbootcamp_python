num_start = int(input("Ingrese el numero inicial: "))
num_end = int(input("Ingrese el numero final: "))

num_odd = []
for num in range(num_start,num_end+1):
   if num % 2 != 0:
      num_odd.append(num)

print(num_odd)