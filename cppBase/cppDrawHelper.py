from turtle import color
import matplotlib.pyplot as plt
from cppBase import cppProblem

def drawProblem(problem):
    mapa_points = problem.map.getPolygon().exterior.coords
    
    if problem.map.has_holes:
        print("Has holes")
        print(problem.map.num_holes)
    else:
        print("No holes")

    plt.plot(*zip(*mapa_points))
    plt.plot(problem.initial_position[0], problem.initial_position[1],  "go")
    plt.plot(problem.final_position[0], problem.final_position[1],  "yo")
    #plt.plot(*zip(*points))
    plt.axis('off')
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.show()


def drawSolution(problem, string_path):

    if problem.map.has_holes:
        print("Has holes")
        print(problem.map.num_holes)
        for i in range(problem.map.num_holes):
            polyi = problem.map.holes[i]
            points = polyi.exterior.coords
            plt.plot(*zip(*points), color = 'grey')
    else:
        print("No holes")

    mapa_points = problem.map.getPolygon().exterior.coords
    plt.plot(*zip(*mapa_points), color = 'grey')
    plt.plot(problem.initial_position[0], problem.initial_position[1],  "go")
    plt.plot(problem.final_position[0], problem.final_position[1],  "yo")
    #plt.plot(*zip(*points))

    points = string_path.coords
    #plt.plot(*zip(*mapa_points))
    plt.plot(*zip(*points))
    plt.axis('off')
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.show()