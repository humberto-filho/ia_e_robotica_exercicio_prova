from aigyminsper.search.search_algorithms import AEstrela
from aigyminsper.search.graph import State
import random


class EntregadorAgent(State):

    def __init__(self, op, mundo):
        super().__init__(op)
        self.pacote = False # comeca sem estar com o pacote
        self.destino = False # comeca sem estar no destino
        self.mundo = mundo # o mundo como o inicializado
        self.pos = [0,0] # posicao inicial
    
    def successors(self):
        if self.destino:
            return []
        successors = []
        x, y = self.pos
        n = len(self.mundo)

        # Pegar pacote
        if self.mundo[x][y] == 4 and not self.pacote:
            novo = EntregadorAgent("pegar pacote", self.mundo)
            novo.pos = [x, y]
            novo.pacote = True
            successors.append(novo)
        # Cima
        if x > 0:
            if self.mundo[x - 1][y] != 3:
                novo = EntregadorAgent("ir cima", self.mundo)
                novo.pos = [x - 1, y]
                novo.pacote = self.pacote
                novo.destino = self.destino
                successors.append(novo)

        # Direita
        if y < n - 1:
            if self.mundo[x][y + 1] != 3:
                novo = EntregadorAgent("ir direita", self.mundo)
                novo.pos = [x, y + 1]
                novo.pacote = self.pacote
                novo.destino = self.destino
                successors.append(novo)

        # Baixo
        if x < n - 1:
            if self.mundo[x + 1][y] != 3:
                novo = EntregadorAgent("ir baixo", self.mundo)
                novo.pos = [x + 1, y]
                novo.pacote = self.pacote
                novo.destino =  self.destino
                successors.append(novo)

        # Esquerda
        if y > 0:
            if self.mundo[x][y - 1] != 3:
                novo = EntregadorAgent("ir esquerda", self.mundo)
                novo.pos = [x, y - 1]
                novo.pacote = self.pacote
                novo.destino = self.destino
                successors.append(novo)

        if self.mundo[x][y] == 5 and self.pacote and not self.destino:
            novo = EntregadorAgent("entregar pacote", self.mundo)
            novo.pos = [x, y]
            novo.pacote = False
            novo.destino = True
            successors.append(novo)

        return successors
    def is_goal(self):
        return self.destino
    
    def description(self):
        return "Problema do Entregador"
    
    def cost(self):
        x, y = self.pos
        if self.mundo[x][y] == 2:
            return 3
        return 1
    
    def env(self):
        return str(self.pos) + "#" + str(self.pacote) + "#" + str(self.destino)

    def h(self):
        n = len(self.mundo)
        destino_x = n - 1
        destino_y = n - 1
        x, y = self.pos

        if self.destino:
            return 1

        if self.pacote:
            return abs(x - destino_x) + abs(y - destino_y) + 1

        for i in range(n):
            for j in range(n):
                if self.mundo[i][j] == 4:
                    distancia_pacote = abs(x - i) + abs(y - j)
                    distancia_destino = abs(i - destino_x) + abs(j - destino_y)
                    return distancia_pacote + distancia_destino + 2

        return 0

def cria_mapa(n):

    # inicializa a matriz com tudo sendo zeros
    matriz = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(1)
        matriz.append(temp)    



    for i in range(n):
        for j in range(n):
            k = random.randint(0, 1000) / 1000.0 # para o pedagio 
            p = random.randint(0, 1000) / 1000.0 # para o obstaculo
            if k <= 0.08:
                matriz[i][j] = 2
            elif p <= 0.11:
                matriz[i][j] = 3
    while True:
        pacote_x = random.randint(0, n-1)
        pacote_y = random.randint(0, n-1)
        if (pacote_x, pacote_y) != (0, 0) and (pacote_x, pacote_y) != (n-1, n-1):
            break

    matriz[0][0] = 1 # garante que nao tem nada no inicio
    matriz[pacote_x][pacote_y] = 4 # garante que nao tem nada no destino
    matriz[n-1][n-1] = 5 # coloca na posicao final o destino
    return matriz


def main():
    print('Algoritmo A estrela')
    n = int(input("Qual o tamanho do mapa?"))

    mundo = cria_mapa(n)

    for linha in mundo:
        print(linha)

    state = EntregadorAgent('', mundo)
    algorithm = AEstrela()
    result = algorithm.search(state, pruning='general')
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()