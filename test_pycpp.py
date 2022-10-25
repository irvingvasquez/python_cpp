from cppBase.cppMap import cppMap
from cppBase.cppMap import drawMap
from shapely.geometry import Point, Polygon
from cppBase.cppRobot import cppRobot
from cppBase.cppProblem import cppProblem
from geometricPlanners.contourPlanner import contourPlanner
from geometricPlanners.cppDisjointPlanner import cppDisjointPlanner
from cppBase.io import savePathAsCSV
import cppBase.cppDrawHelper as dw

import matplotlib.pyplot as plt
import sys, getopt
import numpy as np

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
    print("\nInstituto Politécnico Nacional")
    print('Python based coverage path planning')

    for opt, arg in opts:
        if opt == '-h':
            print('test_contour.py -f <config_folder>')
            sys.exit()
        elif opt in ('-f', '--ffolder'):
            folder = arg
        else:
            sys.exit()

    print('\n------- Configuration -------')
    print('Folder: ', folder)

        
    mapota = cppMap()
    mapota.initializeFromFolder(folder)

    #drawMap(mapota)
    mapa_points= mapota.getPolygon().exterior.coords

    robot = cppRobot()
    robot.initializeFromFolder(folder)

    problema = cppProblem(mapota, robot)
    problema.initializeFromFolder(folder)

    planner = cppDisjointPlanner(problema, verbose=True)
    planner.initializeFromFolder(folder)

    path = planner.plan()
    print("distance:", path.length)

    dw.drawSolution(problema, path)

    outpath = folder + 'solution_path.csv'
    savePathAsCSV(path.coords, outpath)

    outpath = folder + 'distance.csv'
    np.savetxt(outpath, np.array([path.length]), delimiter=',')


if __name__ == "__main__":
    main(sys.argv[1:])


