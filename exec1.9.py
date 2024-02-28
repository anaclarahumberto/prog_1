import math
numero = int(input("Digite um número:"))
rad = math.radians(numero)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f"O seno do número {numero} é {seno:.2f}")
print(f"O cosseno do número {numero} é {cosseno:.2f}")
print(f"O tangente do número {numero} é {tangente:.2f}")
