
import random
import matplotlib.pyplot as plt

N = 9
MIRROR = [
    1, 2, 3, 
    8, 0, 4, 
    7, 6, 5
]

def start_algorith(SEED = 1, tamanho_populacao = 100, geracoes = 1000, taxa_mutacao = 0.1 ):
    random.seed(SEED)
    return algoritmo_genetico(taxa_mutacao, tamanho_populacao, geracoes)


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
def algoritmo_genetico(taxa_mutacao, tamanho_populacao, geracoes ):
    populacao = [criar_individuo() for _ in range(tamanho_populacao)]
    historico_fitness = []
    
    for geracao in range(geracoes):
        melhor_individuo = min(populacao, key=lambda ind: calcular_fitness(ind))
        melhor_fitness = calcular_fitness(melhor_individuo)
        historico_fitness.append(melhor_fitness)

        if melhor_fitness == 0:
            print(f"População: {tamanho_populacao} Gerações: {geracoes} Solução encontrada na geração {geracao}: {melhor_individuo}")
            break

        nova_populacao = selecao(populacao)

        while len(nova_populacao) < tamanho_populacao:
            pai1, pai2 = random.sample(nova_populacao, 2)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho, taxa_mutacao)
            nova_populacao.append(filho)

        populacao = nova_populacao

    if melhor_fitness != 0:
        print(f"População: {tamanho_populacao} Gerações: {geracoes} Solução não encontrada {geracao}: {melhor_individuo}")
        
    return historico_fitness

results = []

results.append(start_algorith(30, 100, 50, 0.1))
results.append(start_algorith(30, 100, 50, 0.25))
results.append(start_algorith(22, 10, 300, 0.15))
results.append(start_algorith(22, 10, 300, 0.3)) 
results.append(start_algorith(1, 1000, 20, 0.15))
results.append(start_algorith(1, 1000, 20, 0.3))


for i, result in enumerate(results):
    plt.figure()  
    plt.plot(result)
    plt.title(f'Evolução do Fitness ao Longo das Gerações (Resultado {i+1})')
    plt.xlabel('Geração')
    plt.ylabel('Fitness (Menor é melhor)')
    plt.grid(True)
    plt.show()

