from models import *

FAILURE = "failure"
CUTOFF = "cutoff"

def depth_limited_search(problem, l):
    
    frontier = [Node(problem.initial)] 
    result = FAILURE
    
    while frontier:
        node = frontier.pop() # LIFO queue (Stack)
        
        if problem.is_goal(node.state):
            return node
        
        # Si el nodo actual excede el límite l
        if node.depth == l:
            result = CUTOFF
        
        # Si no es un ciclo, expandimos (importante para no quedar en bucles)
        elif not is_cycle(node):
            for child in problem.expand(node):
                frontier.append(child)
                
    return result