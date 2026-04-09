# Representación de un grafo en Python
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


def dls(nodo, objetivo, limite):
    print(f"Visitando nodo: {nodo} (Límite restante: {limite})")
    
    if nodo == objetivo:
        return True
    
    if limite <= 0:
        return False
    
    # Explorar vecinos (hijos)
    for vecino in grafo.get(nodo, []):
        if dls(vecino, objetivo, limite - 1):
            return True
            
    return False

# Ejecución
resultado = dls('A', 'F', limite=2)
print(f"¿Objetivo encontrado?: {resultado}")