'''
Copyright 2022 Juan Irving vasquez (jivg.org)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from cppBase.cppSolver import cppSolver
from cppBase.cppProblem import cppProblem
from shapely.geometry import Polygon, Point, LineString
from shapely.geometry import LineString

class contourPlanner(cppSolver):
    def __init__(self, problem) -> None:
        super().__init__(problem)

    def plan(self):
        remaining_contour =  LineString(Polygon(self.problem.map.getPolygon()).exterior.coords)
        print(remaining_contour)
        # validate that the map is convex

        
        # create inner contours
        offset = self.problem.getLateralDelta()
        remaining_contour = remaining_contour.parallel_offset(offset, 'left')

        # while the remaining map has a span bigger that the minimum radius

        init = Point(self.problem.initial_position)
        path_points = [self.problem.initial_position]# + remaining_contour.coords
        for coordinate in remaining_contour.coords:
            path_points.append(coordinate)
        path_points.append(self.problem.final_position)
        
        print(path_points)
        path = LineString(path_points)

        return path


    