numero_1 = int(input("Digite o primeiro número inteiro:"))
numero_2 = int(input("Digite o segundo número inteiro:"))
numero_3 = int(input("Digite o terceiro número inteiro:"))
numero_4 = int(input("Digite o quarto número inteiro:"))
numero_5 = int(input("Digite o quinto número inteiro:"))

if numero_1 % 2 == 0 and numero_2 % 2 == 0 and numero_3 % 2 == 0 and numero_4 % 2 == 0 and numero_5 % 2 == 0:
    print("Todos os números digitados são pares!")
else:
    print("Há pelo menos um número ímpar!")
    
