velocidade_inical = float(input("Digite a velocidade inical (km/h):"))
velocidade_final = float(input("Digite a velocidade final (km/h):"))
tempo_transicao = float(input("Digite o tempo de transição entre as velocidades (s):"))

velocidade_inical_ms = velocidade_inical * 1000 / 3600
velocidade_final_ms = velocidade_final * 1000 / 3600
aceleracao = (velocidade_final_ms - velocidade_inical_ms) / (tempo_transicao - 0)
print(f"A aceleração é de {aceleracao:.2f} m/s²")

