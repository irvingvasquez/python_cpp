'''
Copyright 2022 Juan Irving vasquez (jivg.org)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import configparser
from shapely.geometry import Polygon

class cppRobot():
    def __init__(self, shape, foot_print) -> None:
        self.shape = shape
        self.foot_print = foot_print
        self.foot_print_min_radius = 0

    def __init__(self) -> None:
        self.shape = Polygon
        self.foot_print = Polygon
        self.foot_print_min_radius = 0

    def getFootPrint(self):
        return self.foot_print

    def getFootPrintMinRadius(self):
        return self.foot_print_min_radius

    def initializeFromFolder(self, folder):
        ini_file = folder + "cpp_problem.ini"
        config = configparser.ConfigParser()
        config.read(ini_file)

        self.foot_print_min_radius = float(config['ROBOT']['foot_print_min_radius'])


        # TODO
        # load map shape
        #map_file = folder + "/map.csv"
        #self.map = io.loadPolygonFromCSV(map_file)
        