def es_bisiesto(n):
   if n % 4 == 0:
      if n % 100 == 0:
         if n % 400 == 0:
            return True
         else:
            return False
   else:
      return False
      
print(es_bisiesto(2000))
print(es_bisiesto(2022))