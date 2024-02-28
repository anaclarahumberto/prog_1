dicionario = {}
chave = ""
valor = ""

while True:
    chave = input("Digite o nome do aluno (stop para parar): ")
    if chave != "stop":
        valor =float(input("Digite a nota do aluno: "))
        dicionario[chave] = valor 
    else:
        break

notas_arredondadas = {chave: round(valor) for chave, valor in dicionario.items()}

print("Dicionário de alunos e suas notas respectivamente:")
print(dicionario)

print("Dicionário de alunos e suas notas arredondadas:")
print(notas_arredondadas)





