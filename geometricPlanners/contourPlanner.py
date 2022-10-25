'''
Copyright 2022 Juan Irving vasquez (jivg.org)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from tabnanny import verbose

from numpy import poly
from cppBase.cppSolver import cppSolver
from cppBase.cppProblem import cppProblem
from shapely.geometry import Polygon, Point, LineString
from shapely.geometry import LineString, LinearRing
from geometricPlanners.cppGeometry import getNearestVertexToRing

class contourPlanner(cppSolver):
    def __init__(self, problem, verbose = False) -> None:
        super().__init__(problem)
        self.verbose = verbose

    def plan(self):
        polygon_contour =  LinearRing(Polygon(self.problem.map.getPolygon()).exterior.coords)
        initial_lenght = polygon_contour.length
        erosion_side = 'left'

        if self.verbose:
            print("Polygon contour: ", polygon_contour)
        # validate that the map is convex

        # add initial position
        init = Point(self.problem.initial_position)
        path_points = [self.problem.initial_position]
        
        # define positions
        offset = self.problem.getLateralDelta()
        initial_offset = self.problem.getLateralWallDistance() 

        # make wall offset
        if initial_offset > 0: # validation
            remaining_contour = polygon_contour.parallel_offset(initial_offset, erosion_side)
            if remaining_contour.length > initial_lenght:
                print('Contour Planner Warning: polygon defined clock-wise')
                #erosion_side = 'right'
                remaining_contour = polygon_contour.parallel_offset(initial_offset, 'right')
        else:
            remaining_contour = polygon_contour
            # test if polygon is defined counterclockwise
            #temp_contour = polygon_contour.parallel_offset(initial_offset, erosion_side)
            #if temp_contour.length > initial_lenght:
            #    #erosion_side = 'right'
            #    print('Contour Planner Warning: polygon defined clock-wise')

        if self.verbose:
            print("Target contour: ", remaining_contour)

        current_lenght = remaining_contour.length

        # while the remaining map has a span bigger that the minimum radius
        # sinplified with the line lenght
        while remaining_contour.length > 0:
            
            # shift the contour to connect with the starting position
            #print(remaining_contour.coords)
            nv, md, n_idx = getNearestVertexToRing(init, remaining_contour)
            #print(nv, n_idx)
            shifted_coords = [coordinate for coordinate in remaining_contour.coords[n_idx:-1]]
            for coordinate in remaining_contour.coords[:n_idx+1]:
                shifted_coords.append(coordinate)
            #print(shifted_coords)
            remaining_contour = LinearRing(shifted_coords)

            # include the contour to the path
            for coordinate in remaining_contour.coords:
                path_points.append(coordinate)

            # offset
            remaining_contour = remaining_contour.parallel_offset(offset, erosion_side)
            if remaining_contour.length > current_lenght:
                print('Contour Planner Warning: polygon defined clock-wise')
                #erosion_side = 'right'
                remaining_contour = polygon_contour.parallel_offset(initial_offset, 'right')

            current_lenght = remaining_contour.length

        path_points.append(self.problem.final_position)

        #print(path_points)
        path = LineString(path_points)

        return path


    