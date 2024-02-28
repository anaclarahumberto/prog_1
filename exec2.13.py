idade = int(input("Digite sua idade:"))
sexo = input("Digite seu sexo (M ou F):")

if (idade >= 60 and sexo == 'F') or (idade >= 65 and sexo == 'M'):
    print("Você está legível para aposentadoria!")
else:
    print("Você não está legível para aposentadoria!")

