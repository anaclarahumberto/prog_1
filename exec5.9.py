entrada_usuario = input("Digite uma lista de nomes separados por espaço para que retorne os nomes em caixa alta: ")

lista_nomes = entrada_usuario.split()

nomes_em_caixa_alta = list(map(str.upper, lista_nomes))

print("Lista original:", lista_nomes)
print("Nomes em caixa alta:", nomes_em_caixa_alta)
