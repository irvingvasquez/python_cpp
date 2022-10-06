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

    def __init__(self) -> None:
        self.map = Polygon()

    def isConvex(self):
        return True

    def getPolygon(self):
        return self.map

    def initializeFromFolder(self, folder):
        print("--- Map configuration ---")
        # load map shape
        map_file = folder + "map.csv"
        print("Map file: ", map_file)
        self.map = io.loadPolygonFromCSV(map_file)

