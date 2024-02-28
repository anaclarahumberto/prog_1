palavra = input("Digite uma palavra:") 
palindromo = palavra[::-1] #inverte a string inteira [::-1] 
if palavra == palindromo:
    print("Essa palavra é um palíndromo!")
else:
    print("Essa palavra não é um palíndromo!")
