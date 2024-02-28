numeros = list(range(31))
divisiveis = list(filter(lambda x: x%3==0 or x%5==0, numeros ))
print("Os números de 0 a 30, divisíveis por 3 ou 5 são:", divisiveis) 
