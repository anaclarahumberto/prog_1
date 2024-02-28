nota_1 = float(input("Digite a primeira nota do aluno:"))
nota_2 = float(input("Digite a segunda nota do aluno:"))
nota_3 = float(input("Digite a terceira nota do aluno:"))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
    
if nota_1 == 10 or nota_2 == 10 or nota_3 == 10:
    print("Parabéns!")
