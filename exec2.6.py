texto = "arara"
texto_invertido = texto[::-1] # diz que vai do extremo, ou seja, final, ao início (de trás para frente)

# texto[10:3:-1] diz que vai do nove (uma casa do limite a menos) ao três, de trás para frente
# texto[0:5:2] vai do zero ao quatro (uma casa a menos do limite),pulando de duas em duas casas 

if texto == texto_invertido:
    print("É palíndromo") 
else:
    print("Não é palíndromo")
