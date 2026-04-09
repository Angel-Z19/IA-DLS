from models import Problem
from algorithms import depth_limited_search

grafo = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
problema = Problem(initial_state = 'A', goal_state = 'D', graph = grafo)

resultado = depth_limited_search(problema, l = 0)
print(f"Resultado: {resultado}")