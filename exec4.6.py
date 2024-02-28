print("Insira o primeiro número complexo:")
real_1 = float(input("Digite a parte real: "))
imag_1 = float(input("Digite a parte imaginária: "))
num_1 = complex(real_1, imag_1)

print("Insira o segundo número complexo:")
real_2 = float(input("Digite a parte real: "))
imag_2 = float(input("Digite a parte imaginária: "))
num_2 = complex(real_2, imag_2)

soma = num_1 + num_2
produto = num_1 * num_2

print(f"\nA soma dos números complexos é: {soma}")
print(f"O produto dos números complexos é: {produto}")
