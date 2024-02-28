numero1 = int(input("Digite o primeiro número (a):"))
numero2 = int(input("Digite o segundo número (b):"))
numero3 = int(input("Digite o terceiro número (c):"))
# (b^2) - 4*a*c
delta = (numero2**2) - 4 * numero1 * numero3
x1 = ((-1*numero2) + (delta **(1/2))) / (2*numero1)
x2 = ((-1*numero2) - (delta **(1/2))) / (2*numero1)
print(f"As raízes da fórmula de bhaskara desses números são {x1} e {x2}")

