#Hill climbing algorithm for TSP
import random

#Function to generate a random solution
def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution 
    
#Function to calculate the length of a route
def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength

#Function to get all neighbours of a solution
def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

#Function to get the best neighbour of a solution
def getBestNeighbour(tsp, neighbours):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

#Function to apply hill climbing to a solution
def hillClimbing(tsp, initialState):
    currentSolution = initialState
    currentRouteLength = routeLength(tsp, currentSolution)
    print("Current Solution: ", currentSolution, "  Route Length: ", currentRouteLength)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        print("Current Solution: ", currentSolution, "  Route Length: ", currentRouteLength)
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    return currentSolution, currentRouteLength

#Main function
def main():
    tsp = [
        [0, 4, 5, 3, 7, 8, 1],
        [4, 0, 3, 5, 2, 2, 6],
        [5, 3, 0, 4, 1, 3, 3],
        [3, 5, 4, 0, 3, 4, 1],
        [7, 2, 1, 3, 0, 5, 1],
        [8, 2, 3, 4, 5, 0, 1],
        [1, 6, 3, 1, 1, 1, 0]
    ]

    initialState = randomSolution(tsp)
    print("Initial State: ", initialState )
    print("------------------ Search ------------------")
    solution, routeL = hillClimbing(tsp,initialState)
    print("--------------------------------------------")
    print("Best Route: ", solution)
    print("Route Length: ", routeL)

if __name__ == "__main__":
    main()


