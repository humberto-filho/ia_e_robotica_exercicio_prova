### IA e Robótica APS4 Exercício de prova

#### Membros:
- Humberto Filho Castello Branco Lages Rebello e Castro

Nesse exercício irei apresentar uma solução para o problema proposto nos links abaixo:
- <a href="https://insper.github.io/ia_bcc/aulas/16_revisao_prova/prova/"> Enunciado da Prova </a>
- <a href="https://insper.github.io/ia_bcc/aulas/16_revisao_prova/prova/"> Enunciado da APS </a>

O mundo é descrito como:
- 
<img src="grid_mundo_10x10.png" width=30%/>

- 

O arquivo principal é o main.py. Nele também se encontra a função cria_mapa(n) que recebe o argumento n (tamanho do mapa)
e cria um mapa semelhante ao da imagem supracitada. Nele, aproximadamente 8% das casas são pedágios e 11% das casas
são obstáculos, com um pacote num local aleatório, entregador inicialmente em (0,0) e pacote em (n-1, n-1) (0 indexado).

Ele usa o algoritmo A Estrela com uma heurística baseada na distância de manhattan definida por:
$$
    \begin{cases}
    h(n) = d(atual, pacote) + d(pacote, destino) + 2 \\ 
    h(n) = d(atual, destino) + 1 \\ 
    h(n) = 0 \\ 
    \end{cases}
$$

Para, respectivamente: antes de pegar a encomenda, após pegar a encomenda e após deixar a encomenda ao destino.

O entregador pode se mover com custo 1, se mover com pedágio irá ocasionar em custo 3 (custo + 2), pegar a encomenda e entregar ela ao destino também terá custo 1.



