idade = int(input("Digite a idade sua idade:"))
nacionalidade = input("Digite sua nacionalidade: ")

if idade >= 18 and (nacionalidade == 'Brasil' or 'brasil'): 
    print("Você pode votar!")
else:
    print("Você não pode votar!")
    
