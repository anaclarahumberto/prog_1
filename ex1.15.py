def tempo_queda (distancia, velocidade_inical):
    gravidade = 10
    tempo = (2 * distancia / gravidade) ** 0.5
    tempo -= velocidade_inical / gravidade
    return tempo

distancia = float(input("Digite a distância em metros do objeto em queda livre:"))
velocidade_inical = float(input("Digite a velocidade inical do objeto em queda livre em m/s:"))

tempo = tempo_queda(distancia, velocidade_inical)
print(f"O tempo que o objeto leva para atingir o solo é de {tempo:.2f} segundos")

    
