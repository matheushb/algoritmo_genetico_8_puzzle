
import random
import matplotlib.pyplot as plt

# Numero de rainhas (tamanho tabuleiro) e seed para o random
N = 9
SEED = 99
MIRROR = [
    1, 2, 3, 
    8, 0, 4, 
    7, 6, 5
    ]
random.seed(SEED)

# Gerando um individuo aleatorio
def criar_individuo():
    return random.sample(range(N), N)


# cálculo do fitness
def calcular_fitness(individuo):
    conflitos = 0
    for i in range(N):
        conflitos += abs(MIRROR[i] - individuo[i])
    return conflitos

# Seleção dos melhores individuos
def selecao(populacao):
    populacao.sort(key=lambda ind: calcular_fitness(ind))
    return populacao[:len(populacao)//2]  # Retorna a metade superior da população

# Crossover com ponto de corte aleatorio
def crossover(pai1, pai2):
    ponto_corte = random.randint(0, N-1)
    filho = pai1[:ponto_corte] + pai2[ponto_corte:]
    return filho

# Mutacao com uma taxa de 0.1
def mutacao(individuo, taxa_mutacao=0.1):
    if random.random() < taxa_mutacao:
        i = random.randint(0, N-1)
        individuo[i] = random.randint(0, N-1)
    return individuo

# execucao do AG
def algoritmo_genetico(tamanho_populacao=100, geracoes=1000):
    populacao = [criar_individuo() for _ in range(tamanho_populacao)]
    historico_fitness = []
    print(populacao)
    
    for geracao in range(geracoes):
        melhor_individuo = min(populacao, key=lambda ind: calcular_fitness(ind))
        melhor_fitness = calcular_fitness(melhor_individuo)
        historico_fitness.append(melhor_fitness)

        if melhor_fitness == 0:
            print(f"Solução encontrada na geração {geracao}: {melhor_individuo}")
            break

        nova_populacao = selecao(populacao)

        while len(nova_populacao) < tamanho_populacao:
            pai1, pai2 = random.sample(nova_populacao, 2)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho)
            nova_populacao.append(filho)

        populacao = nova_populacao

    # Plotando o gráfico de fitness ao longo das gerações
    plt.plot(historico_fitness)
    plt.title('Evolução do Fitness ao Longo das Gerações')
    plt.xlabel('Geração')
    plt.ylabel('Fitness (Menor é melhor)')
    plt.show()

    return melhor_individuo

# Executar o algoritmo
solucao = algoritmo_genetico()

print("Solucao: ",solucao)