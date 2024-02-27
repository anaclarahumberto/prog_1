frase = input("Digite uma frase: ")
palavras = frase.split()
contem_a = filter (lambda p: p.find("a")>=0, palavras)
novo_texto = [p.replace("a", "o") for p in palavras]
print(" ".join (novo_texto))