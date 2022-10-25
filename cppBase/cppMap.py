'''
Copyright 2022 Juan Irving vasquez (jivg.org)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import cppBase.io as io
import configparser

def plotPolygons(polygons):
    fig, ax = plt.subplots(1)
    for element in polygons:
        points = element.exterior.coords.xy
        
        points = np.transpose(points)
        polygon_shape = matplotlib.patches.Polygon(points, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(polygon_shape)
        plt.axis("equal")
    plt.show()


def drawMap(map):
    plotPolygons([map.getPolygon()])


class cppMap():
    def __init__(self, polygonal_map) -> None:
        self.map = polygonal_map
        self.initialized = False
        self.is_convex = False
        self.has_holes = False
        self.num_holes = 0
        self.holes = []

    def __init__(self) -> None:
        self.map = Polygon()
        self.initialized = False
        self.is_convex = False
        self.has_holes = False
        self.num_holes = 0
        self.holes = []

    def isConvex(self):
        return self.is_convex

    def getPolygon(self):
        return self.map

    def initializeFromFolder(self, folder):
        print("--- Map configuration ---")
        # load map shape
        map_file = folder + "map.csv"
        print("Map file: ", map_file)
        self.map = io.loadPolygonFromCSV(map_file)

        ini_file = folder + "cpp_problem.ini"
        config = configparser.ConfigParser()
        try:
            config.read(ini_file)
        except:
            print("Error reading file")
            exit(0)

        self.is_convex = bool(config['MAP']['is_convex'])
        print("Is convex: ", self.is_convex)
        #self.is_convex = bool(config['MAP']['is_convex'])
        #print("Has holes: ", self.has_holes)
        self.has_holes = bool(config['MAP']['has_holes'])
        print("Has holes: ", self.has_holes)

        if self.has_holes:
            self.num_holes = int(config['MAP']['num_holes'])
            print("Number of holes: ", self.num_holes)

            for i in range(self.num_holes):
                hole_file = folder + "hole_" + str(i) + ".csv"
                print("Hole file: ", hole_file)
                temp_poly = io.loadPolygonFromCSV(hole_file)
                self.holes.append(temp_poly)

        self.initialized = True

