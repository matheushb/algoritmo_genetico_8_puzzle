# Resumo sobre o 8 Puzzle com Algoritmo Genético

O **8 Puzzle** é um problema clássico de programação combinatorial onde o objetivo é reorganizar peças numeradas de 1 a 8 em um tabuleiro de 3x3 para que as peças fiquem em suas posições corretas. O jogo possui uma peça vazia que permite movimentar as outras peças horizontalmente ou verticalmente. O problema é considerado **NP-completo**, o que significa que encontrar uma solução exata é difícil para grandes instâncias.

## Algoritmo Genético

O código implementa uma abordagem de **Algoritmo Genético (AG)** para resolver o 8 Puzzle. O AG é uma técnica de otimização inspirada nos processos de evolução biológica, como seleção natural, crossover e mutação. O objetivo é encontrar uma solução próxima do ideal por meio de um processo iterativo.

### Componentes principais do Algoritmo Genético:

#### Indivíduo:

Um indivíduo é representado como uma lista de 9 números que corresponde à configuração atual do tabuleiro do 8 Puzzle.  
A função `criar_individuo` gera um indivíduo aleatoriamente, que representa uma possível solução para o problema.

#### Função Fitness:

A função `calcular_fitness` avalia a qualidade de cada indivíduo, calculando o número de conflitos, ou seja, a diferença absoluta entre a posição atual e a posição desejada de cada peça.  
O **fitness** serve como métrica para guiar o processo de evolução do AG. Quanto menor o valor do fitness, melhor a solução.

#### Seleção:

A função `selecao` ordena os indivíduos da população de acordo com seu fitness e seleciona os melhores para a próxima geração, mantendo a metade superior da população.

#### Crossover:

A função `crossover` combina dois indivíduos (pais) para gerar um novo indivíduo (filho) por meio de um ponto de corte aleatório. Isso permite a troca de genes entre os pais.

#### Mutação:

A função `mutacao` modifica um gene aleatório de um indivíduo com uma pequena probabilidade, introduzindo diversidade na população e ajudando a explorar mais soluções possíveis.

### Execução do Algoritmo Genético:

A função `algoritmo_genetico` gera uma população inicial, avalia o fitness dos indivíduos, realiza seleção, crossover e mutação até encontrar uma solução com fitness zero (ou uma solução próxima). A solução é encontrada quando o tabuleiro está perfeitamente ordenado.
O histórico de fitness ao longo das gerações é retornado para análise.

### Visualização dos Resultados:

O código gera gráficos que mostram a evolução do fitness ao longo das gerações. Cada gráfico representa a execução de diferentes parâmetros do algoritmo (como tamanho da população, taxa de mutação e número de gerações). Após o fechamento de um gráfico, o próximo é exibido.
