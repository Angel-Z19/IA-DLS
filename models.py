class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

    def __repr__(self):
        return f"Node({self.state}, depth={self.depth})"

class Problem:
    def __init__(self, initial_state, goal_state, graph):
        self.initial = initial_state
        self.goal = goal_state
        self.graph = graph

    def is_goal(self, state):
        return state == self.goal
    
    def expand(self, node):
        children = []
        for succesor in self.graph.get(node.state, []):
            children.append(Node(succesor, parent=node, depth=node.depth + 1))
        return children


def is_cycle(node):
        #Verifica si el estado del nodo ya existe en su línea de ancestros."
    current = node.parent
    while current:
        if current.state == node.state:
            return True
        current = current.parent
    return False