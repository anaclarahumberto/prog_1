import nltk
nltk.download('punkt')

while True:
    texto = input("Digite uma frase com 5 palavras: ")
    palavras = nltk.word_tokenize(texto)
    
    if len(palavras) != 5: 
        print("Você digitou uma frase com uma quantidade diferente de palavras. Por favor, digite uma frase com exatamente 5 palavras.")
    else: 
        for i in palavras:
            print(i)
        break
