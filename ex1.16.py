valor_inicial = float(input("Digite o valor inicial do investimento:"))
taxa_juros = float(input("Digite a taxa de juros:"))
numero_anos = int(input("Digite o número de anos:"))

juros_compostos = valor_inicial * (1+taxa_juros)**numero_anos
print(f"O valor final do investimento foi de R${juros_compostos}")