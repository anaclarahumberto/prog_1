entrada = input("Digite um número real: ")
e_numero_real = True

for caractere in entrada:
    if not (caractere.isdigit() or caractere == '.'):
        e_numero_real = False
        break

if e_numero_real:
    pontos_decimais = entrada.count('.')
    if pontos_decimais != 1:
        e_numero_real = False

if e_numero_real:
    print("É um número real.")
else:
    print("Não é um número real.")
