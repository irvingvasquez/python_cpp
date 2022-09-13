from pickle import TRUE
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


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

    def isConvex(self):
        return TRUE

    def getPolygon(self):
        return self.map

    
