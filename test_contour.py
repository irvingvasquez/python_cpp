from cppBase.cppMap import cppMap
from cppBase.cppMap import drawMap
from shapely.geometry import Point, Polygon
from cppBase.cppRobot import cppRobot
from cppBase.cppProblem import cppProblem
from geometricPlanners.contourPlanner import contourPlanner

import matplotlib.pyplot as plt


def main():
    print("Hello World!")

    folder = './data/convex_polygon_example'
    mapota = cppMap()
    mapota.initializeFromFolder(folder)

    drawMap(mapota)

    robot = cppRobot()
    robot.initializeFromFolder(folder)

    problema = cppProblem(mapota, robot)
    problema.initializeFromFolder(folder)

    planner = contourPlanner(problema)

    path = planner.plan()

    points = path.coords
    

    plt.plot(*zip(*points))
    plt.show()
    

if __name__ == "__main__":
    main()


