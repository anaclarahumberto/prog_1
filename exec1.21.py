comprimento_lado1=float(input("Digite o comprimento de um dos lados de um triangulo retângulo: "))
comprimento_lado2=float(input("Digite o comprimento do outro lado:"))

hipotenusa_ao_quadrado= (comprimento_lado1**2) + (comprimento_lado2**2)
hipotenusa= hipotenusa_ao_quadrado**0.5

print(" A hipotenusa vale:",hipotenusa)
