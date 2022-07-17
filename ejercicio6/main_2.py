def es_primo(n):
   if n == 1:
      return False
   if n == 2:
      return True
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

print(es_primo(10))
print(es_primo(7))