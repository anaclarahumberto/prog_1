distancia_percorrida = float(input("Digite a distância percorrida pelo objeto em (m):"))
tempo_gasto = float(input("Digite o tempo gasto pelo objeto em (s):"))
aceleracao = float(input("Digite a aceleração em (m/s²):"))

velocidade_inicial = distancia/tempo - aceleracao * tempo / 2 
velocidade_final = velocidade_inicial + aceleracao * tempo_gasto
print("A velocidade inicial do objeto é ", velocidade_inicial, "m/s², e a sua velocidade final é de ",velocidade_final, "m/s².")
