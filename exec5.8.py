entrada_usuario = input("Digite uma lista de números separados por espaço para que seja calculado o quadrado desses números respectivamente: ")

lista_numeros = list(map(float, entrada_usuario.split()))

quadrados = list(map(lambda x: x**2, lista_numeros))

print("Lista original:", lista_numeros)
print("Quadrados:", quadrados)
