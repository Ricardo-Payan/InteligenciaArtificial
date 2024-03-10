import time
class PuzzleState:
    def __init__(self, state:str):
        self.state = state
    def print(self):
        for i in range(1,4):
            line = ""
            for number in self.state[3*(i-1):3*i]:
                line += number + " "
            print(line)
    def __str__(self):
        return self.state



def getSuccessors(puzzle: str):
    possiblesSwaps = {
        0: {1, 3},
        1: {0, 2, 4},
        2: {1, 5},
        3: {0, 4, 6},
        4: {1, 3, 5, 7},
        5: {2, 4, 8},
        6: {3, 7},
        7: {6, 4, 8},
        8: {7, 5}
        } 
    indexOfBlank = puzzle.index("_")
    successors = []
    
    for newPosition in possiblesSwaps[indexOfBlank]:
        newState = list(puzzle)
        newState[indexOfBlank], newState[newPosition] =newState[newPosition],newState[indexOfBlank]
        newState = "".join(newState)
        successors.append(newState)

    return successors
def BFS(puzzle:str, goalState:str):
    nodes = 0
    queue = getSuccessors(puzzle)
    visited = set()
    while len(queue) > 0:
        currentState = queue.pop(0)
        if (currentState == goalState):
            print("Nodos Totales en BFS: " + str(nodes))
            return
        if currentState not in visited:
            nodes += 1
            visited.add(currentState)
            for x in getSuccessors(currentState):
                if x not in visited:
                    queue.append(x)

def DFS(puzzle:str, goalState:str):
    nodes = 0
    stack = getSuccessors(puzzle)
    visited = set()
    while len(stack) > 0:
        currentState = stack.pop()
        if (currentState == goalState):
            # print("found it")
            print("Nodos Totales en DFS: " + str(nodes))
            return
        if currentState not in visited:
            nodes += 1
            visited.add(currentState)
            for x in getSuccessors(currentState):
                if x not in visited:
                    stack.append(x)

def timeFunction(function, toSolve:str, goalState): 
    inicio = time.time()
    function(toSolve, goalState)
    tiempo_final = time.time() - inicio
    print(tiempo_final*1000)



if __name__ == "__main__":
    toSolve = [PuzzleState("123456_78"), PuzzleState("3_7281645"), PuzzleState("5318246_7")]
    printgoal = PuzzleState("12345678_").print()
    goalState = "12345678_"
    for state in toSolve:
        state.print() 
        print()

    for state in toSolve:
        timeFunction(DFS, str(state), goalState)
        timeFunction(BFS, str(state), goalState)
