numero1 = int(input("Digite um número para (a):"))
numero2 = int(input("Digite um número (b):"))
numero3 = int(input("Digite um número (c):"))

delta = (numero2**2) - 4 * numero1 * numero3
x1 = ((-1*numero2) + (delta **(1/2))) / (2*numero1)
x2 = ((-1*numero2) - (delta **(1/2))) / (2*numero1)
print(f"As raízes da fórmula de bhaskara desses números são {x1} e {x2}")

