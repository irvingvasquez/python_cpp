from cppBase.cppMap import cppMap
from cppBase.cppMap import drawMap
from shapely.geometry import Point, Polygon
from cppBase.cppRobot import cppRobot
from cppBase.cppProblem import cppProblem
from geometricPlanners.contourPlanner import contourPlanner

import matplotlib.pyplot as plt
import sys, getopt

def main(argv):
    if len(argv)==0:
        print('test.py -f <config_folder>')
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv,"hf:",["ffolder="])
    except getopt.GetoptError:
        print('test.py -f <config_folder>')
        sys.exit(2)

    #folder = './data/convex_polygon_example/'

    for opt, arg in opts:
        if opt == '-h':
            print('test_contour.py -f <config_folder>')
            sys.exit()
        elif opt in ('-f', '--ffolder'):
            folder = arg
        else:
            sys.exit()
        
    mapota = cppMap()
    mapota.initializeFromFolder(folder)

    #drawMap(mapota)
    mapa_points= mapota.getPolygon().exterior.coords

    robot = cppRobot()
    robot.initializeFromFolder(folder)

    problema = cppProblem(mapota, robot)
    problema.initializeFromFolder(folder)

    planner = contourPlanner(problema)

    path = planner.plan()

    points = path.coords
    
    plt.plot(*zip(*mapa_points))
    plt.plot(*zip(*points))
    plt.show()
    

if __name__ == "__main__":
    main(sys.argv[1:])


