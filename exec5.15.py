numeros = [float(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
escolha = float(input("Digite um número de referência: "))
posicao = next((i for i, num in enumerate(numeros) if num > escolha), None)
if posicao is not None:
    print("A posição do primeiro elemento maior que",escolha,"é:",posicao)
else:
    print("Nenhum elemento na lista é maior que:", escolha)
