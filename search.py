"""
Integrantes del grupo: 
Natalia Guerrero Caicedo
Alejandro Ayala
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    """
    PUNTO 1
    Idea general:
        Iterar hasta que se llegue a un estado final (goal state)
            -> problem.isGoalState(problem.getStartState())

        Start: (9, 1)
        Is the start a goal? False
        Start's successors: [((10, 1), 'East', 1), ((8, 1), 'West', 1)]

        ((10, 1), 'East', 1) ->

        ((8, 1), 'West', 1) <-

        return ['East'] -> Estilo del retorno debe ser ese
    """

    camino = [] ## Esta lista contiene la respuesta del camino
    antecesor = dict() ## Diccionario que me dice cuál es el antecesor de un estado
    visitados = dict() ## Diccionario que me dice si un estado ya ha sido visitado
    movimientos = dict() ## Diccionario que me dice cuál fue el movimiento que tuve que hacer para llegar a ese estado

    node = problem.getStartState() # #Estado en el que me encuentro
    estadoInicio = problem.getStartState() ## Este es el estado inicial, importante para construir el camino final

    pila = util.Stack() # Esta es la pila
    
    ##Inicio del algoritmo
    pila.push(node) #Se agrega el nodo inicial

    while not pila.isEmpty(): ## Mientras la pila tenga elementos
        node = pila.pop() ## Sacar el tope de la pila
        visitados[node] = True

        if problem.isGoalState(node):
            ## Cuando el nodo sea el estado esperado para finalizar, entonces deja de buscar
            break
        else:
            for sucesores in problem.getSuccessors(node):
                nodoSucesor = sucesores[0]
                movimientoNecesario = sucesores[1]

                if nodoSucesor not in visitados:
                    antecesor[nodoSucesor] = node # Guardo el sucesor
                    movimientos[nodoSucesor] = movimientoNecesario
                    pila.push(nodoSucesor)

    ##Cuando finaliza el ciclo while, se construye el camino

    ##Construyendo el camino

    while node != estadoInicio:
        camino.append( movimientos[node] )
        node = antecesor[node]

    camino.reverse()
    return camino


def breadthFirstSearch(problem):
    ## Solución para el PUNTO 5 | Find all corners
    "*** YOUR CODE HERE ***"
    nodo = problem.getStartState() ## Estado en el que me encuentro

    cola = util.Queue() # Esta es la cola
    cola.push( (nodo, [nodo], [], []) ) # (nodo, visitados, esquinas, camino)

    while not cola.isEmpty():
        state = cola.pop()
        nodo, visitados, esquinas, camino = state[0], state[1], state[2], state[3]

        if problem.isGoalState(esquinas):
            return camino
        else:
            for sucesor in problem.getSuccessors(nodo):
                nodoSucesor = sucesor[0]
                movimiento = sucesor[1]
                if nodoSucesor in problem.corners and nodoSucesor not in visitados and nodoSucesor not in esquinas:
                    cola.push((nodoSucesor, esquinas, esquinas + [nodoSucesor], camino+[movimiento]))
                elif nodoSucesor not in visitados:
                    cola.push((nodoSucesor, visitados + [nodoSucesor], esquinas, camino+[movimiento]))

    return camino
"""
def breadthFirstSearch(problem):
    ## Solución para el PUNTO 2
    "*** YOUR CODE HERE ***"
    camino = [] ## Esta lista contiene la respuesta del camino
    antecesor = dict() ## Diccionario que me dice cuál es el antecesor de un estado
    visitados = dict() ## Diccionario que me dice si un estado ya ha sido visitado
    movimientos = dict() ## Diccionario que me dice cuál fue el movimiento que tuve que hacer para llegar a ese estado

    node = problem.getStartState() ## Estado en el que me encuentro
    estadoInicio = problem.getStartState() ## Este es el estado inicial, importante para construir el camino final

    cola = util.Queue() # Esta es la cola
    
    ##Inicio del algoritmo
    cola.push(node) #Se agrega el nodo inicial
    visitados[node] = True

    while not cola.isEmpty(): ## Mientras la cola tenga elementos
        node = cola.pop() ## Sacar el tope de la cola

        if problem.isGoalState(node):
            ## Cuando el nodo sea el estado esperado para finalizar, entonces deja de buscar
            break
        else:
            for sucesores in problem.getSuccessors(node):
                nodoSucesor = sucesores[0]
                movimientoNecesario = sucesores[1]

                if nodoSucesor not in visitados:
                    visitados[nodoSucesor] = True
                    antecesor[nodoSucesor] = node # Guardo el sucesor
                    movimientos[nodoSucesor] = movimientoNecesario
                    cola.push(nodoSucesor)

    ##Cuando finaliza el ciclo while, se construye el camino

    ##Construyendo el camino

    while node != estadoInicio:
        camino.append( movimientos[node] )
        node = antecesor[node]

    camino.reverse()
    return camino
"""
def uniformCostSearch(problem):
    """ PUNTO 3 """
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    camino = [] ## Esta lista contiene la respuesta del camino
    antecesor = dict() ## Diccionario que me dice cuál es el antecesor de un estado
    movimientos = dict() ## Diccionario que me dice cuál fue el movimiento que tuve que hacer para llegar a ese estado
    coste = dict() ## Diccionario que me dice cuál fue el coste para llegar a un nodo

    node = problem.getStartState() ## Estado en el que me encuentro
    estadoInicio = problem.getStartState() ## Este es el estado inicial, importante para construir el camino final

    colaPrioridad = util.PriorityQueue() # Esta es la cola de prioridad
    
    ##Inicio del algoritmo
    colaPrioridad.push(node, 0) #Se agrega el nodo inicial
    coste[node] = 0

    while colaPrioridad: ## Mientras la cola de prioridad tenga elementos
        node = colaPrioridad.pop() ## Sacar el tope de la cola de prioridad

        if problem.isGoalState(node):
            ## Cuando el nodo sea el estado esperado para finalizar, entonces deja de buscar
            break
        else:
            for sucesores in problem.getSuccessors(node):
                nodoSucesor = sucesores[0]
                movimientoNecesario = sucesores[1]
                nuevoCosto = coste[node] + sucesores[2]

                if nodoSucesor not in coste:
                    antecesor[nodoSucesor] = node # Guardo el sucesor
                    movimientos[nodoSucesor] = movimientoNecesario
                    coste[nodoSucesor] = nuevoCosto
                    colaPrioridad.push(nodoSucesor, nuevoCosto)

    ##Cuando finaliza el ciclo while, se construye el camino

    ##Construyendo el camino

    while node != estadoInicio:
        camino.append( movimientos[node] )
        node = antecesor[node]

    camino.reverse()
    return camino

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    PUNTO 4
    """
    "*** YOUR CODE HERE ***"
    camino = [] ## Esta lista contiene la respuesta del camino
    antecesor = dict() ## Diccionario que me dice cuál es el antecesor de un estado
    movimientos = dict() ## Diccionario que me dice cuál fue el movimiento que tuve que hacer para llegar a ese estado
    coste = dict() ## Diccionario que me dice cuál fue el coste para llegar a un nodo

    node = problem.getStartState() ## Estado en el que me encuentro
    estadoInicio = problem.getStartState() ## Este es el estado inicial, importante para construir el camino final

    colaPrioridad = util.PriorityQueue() # Esta es la cola de prioridad
    
    ##Inicio del algoritmo
    colaPrioridad.push(node, 0) #Se agrega el nodo inicial
    coste[node] = 0

    while not colaPrioridad.isEmpty(): ## Mientras la cola de prioridad tenga elementos
        node = colaPrioridad.pop() ## Sacar el tope de la cola de prioridad

        if problem.isGoalState(node):
            ## Cuando el nodo sea el estado esperado para finalizar, entonces deja de buscar
            break
        else:
            for sucesores in problem.getSuccessors(node):
                nodoSucesor = sucesores[0]
                movimientoNecesario = sucesores[1]
                nuevoCosto = coste[node] + sucesores[2]

                if nodoSucesor not in coste or nuevoCosto < coste[nodoSucesor]:
                    antecesor[nodoSucesor] = node # Guardo el sucesor
                    movimientos[nodoSucesor] = movimientoNecesario
                    coste[nodoSucesor] = nuevoCosto
                    colaPrioridad.push(nodoSucesor, nuevoCosto + heuristic(nodoSucesor, problem))

    ##Cuando finaliza el ciclo while, se construye el camino

    ##Construyendo el camino

    while node != estadoInicio:
        camino.append( movimientos[node] )
        node = antecesor[node]

    camino.reverse()
    return camino

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
