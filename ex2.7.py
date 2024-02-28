numero = float(input("Digite um número:"))
string = str(numero)

if string.endswith('.0') or '.' not in string:
    print("É um número inteiro!")
else:
    print("Não é um número inteiro!")

#string.endswith verifica se a string termina com .0 (10.0, 15.0, 20.0, entre outros) 
# ou '.' not in string, verifica se não tem um ponto decimal na string, caso seja verdadeiro, esse número também será inteiro
