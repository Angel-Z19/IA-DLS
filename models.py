class Node:
    def __init__(self, state, parent=None, depth=0, path_cost = 0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.path_cost = path_cost

    def __repr__(self):
        return f"Node({self.state}, depth={self.depth})"
    
    def get_path(self):
        path = []
        current = self
        while current:
            path.append(current.state)
            current = current.parent
        return path[::-1] # Invertimos la lista para que vaya de Inicio a Fin

class Problem:
    def __init__(self, initial_state, goal_state, graph):
        self.initial = initial_state
        self.goal = goal_state
        self.graph = graph

    def is_goal(self, state):
        return state == self.goal
    
    def expand(self, node):
        children = []
        for succesor, distance in self.graph.get(node.state, []):
            new_cost = node.path_cost + distance
            children.append(Node(state = succesor,
                                 parent=node,
                                 depth=node.depth + 1,
                                 path_cost=new_cost))
        return children


def is_cycle(node):
        #Verifica si el estado del nodo ya existe en su línea de ancestros."
    current = node.parent
    while current:
        if current.state == node.state:
            return True
        current = current.parent
    return False