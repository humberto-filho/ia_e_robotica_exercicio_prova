import random

n = int(input())

matriz = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    matriz.append(temp)    

matriz[n-1][n-1] = 5 # coloca na posicao final o destino

for i in range(n):
    for j in range(n):
        k = random.randint(0, 1000) / 1000.0 # para o pedagio 
        p = random.randint(0, 1000) / 1000.0 # para o obstaculo
        if k <= 0.08:
            matriz[i][j] = 2
        elif p <= 0.11:
            matriz[i][j] = 3

pacote_x = random.randint(0, n-1)
pacote_y = random.randint(0, n-1)

matriz[pacote_x][pacote_y] = 4


print(matriz)