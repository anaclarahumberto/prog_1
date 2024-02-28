cateto1 = float(input("Digite o valor do primeiro cateto:"))
cateto2 = float(input("Digite o valor do segundo cateto:"))

hipotenusa = (cateto1**2 + cateto2**2) **0.5 #hipotenusa(base do triângulo retângulo[a])
altura = (cateto1 * cateto2) / hipotenusa #altura da hipotenusa[h]
area = (altura * hipotenusa) / 2 # area = b*h/2
print(f"O valor da área do triângulo retângulo é de {area} cm²")

