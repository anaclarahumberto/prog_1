import math

lista = list (range(21))
raiz_pares = [math.sqrt(x) for x in lista  if x % 2 == 0]
print (raiz_pares)