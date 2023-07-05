def dls(grafo, inicio, meta, limite, profundidade=0):
    if inicio == meta:
        print("Destino alcançado:", meta)
        return True

    if limite == 0:
        return False

    print(f"Visitado: {inicio}, Limite: {limite}")

    vizinhos = grafo.get(inicio, [])

    for prox in vizinhos:
        print(f"Visitado: {prox}, Limite: {limite - 1}")
        encontrou = dls(grafo, prox, meta, limite - 1, profundidade + 1)
        if encontrou:
            return True

    return False


# Criando o grafo
grafo = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Eforie': ['Hirsova'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Neamt': ['Iasi'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Zerind': ['Oradea', 'Arad'],
    'Sibiu': ['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Vaslui': ['Urziceni', 'Iasi']
}

origem = 'Arad'
destino = 'Bucharest'
limite_profundidade = 3

encontrou_destino = dls(grafo, origem, destino, limite_profundidade)

if not encontrou_destino:
    print("O destino não foi alcançado:", destino)
