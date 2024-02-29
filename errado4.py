import math
lista=list(range(21))

raiz=[x **(1/2) for x in lista if x %2==0]

print(raiz)
