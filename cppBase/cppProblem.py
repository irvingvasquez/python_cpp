'''
Copyright 2022 Juan Irving vasquez (jivg.org)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from cppBase.cppRobot import cppRobot
from cppBase.cppMap import cppMap
import configparser

class cppProblem():
    def __init__(self, map, robot) -> None:
        self.map = map
        self.robot = robot
        self.overlap = 0
        self.initial_position = (0.0, 0.0)
        self.final_position = (0.0, 0.0)

    def setOverlap(self, overlap):
        self.overlap = overlap
    
    def getLateralDelta(self):
        #todo
        return self.robot.getFootPrintMinRadius()

    def initializeFromFolder(self, folder):
        ini_file = folder + "cpp_problem.ini"
        config = configparser.ConfigParser()
        config.read(ini_file)

        self.initial_position = (float(config['PROBLEM']['initial_position_x']), float(config['PROBLEM']['initial_position_y']))
        self.final_position = (float(config['PROBLEM']['final_position_x']), float(config['PROBLEM']['final_position_y']))

