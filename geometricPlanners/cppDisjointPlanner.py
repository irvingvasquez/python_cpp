
from importlib.resources import path
from tabnanny import verbose
import numpy as np
from traitlets import All
from cppBase.cppSolver import cppSolver
import configparser
from shapely.geometry import LineString, LinearRing

class cppDisjointPlanner(cppSolver):
    def __init__(self, problem, verbose = False) -> None:
        super().__init__(problem)
        self.verbose = verbose
        self.num_areas = 0
        self.reverse = []
        self.tour = []
        self.initialized = False
        self.folder = ""

    def initializeFromFolder(self, folder):
        self.folder = folder
        ini_file = folder + "cpp_problem.ini"
        config = configparser.ConfigParser()
        try:
            config.read(ini_file)
        except:
            print("Error reading file")
            exit(0)

        print("--- Disjoint Planner Configuration ---")
        self.num_areas = int(config['DISJOINT']['num_areas'])
        print("Number of areas: ", self.num_areas)
        self.initialized = True

    def plan(self):
        if not self.initialized:
            print("DisjointPlanner, Warning: not initialized")
            return

        # Set of coverage paths for each area
        All_paths = []

        for i in range(self.num_areas): 
            # coverage path
            path_file = self.folder + "area_" + str(i) + "\solution_path.csv"
            if self.verbose:
                print("Area path file:", path_file)
            try:
                area_path = np.genfromtxt(path_file, delimiter=',')
            except:
                print("Error reading file: ", path_file)
                exit(0)

            m = 0
            n = 0
            if area_path.ndim == 1:
                n = area_path.shape[0]
                if n > 0:
                    m = 1
                    path = [area_path]
            elif area_path.ndim == 2:
                #TODO: Validation
                #for point in area_path:
                #paths_for_area.append(area_path)
                m, n = area_path.shape
                path = area_path
            
            element = {'area': i, 'len': m, 'path': path}
            All_paths.append(element)

        
        # Path planning
        # Define the structures
        # Tour order
        try:
            tour_file = self.folder + 'tour.csv'
            nptour = np.genfromtxt(tour_file, delimiter=',')
            self.tour = [int(i) for i in nptour]
        except:
            self.tour = [i for i in range(self.num_areas)]
            #print("Error reading file: ", path_file)
            #exit(0)
        
        if (self.verbose):
            print("tour: ", self.tour)
        # Defines if a section is reversed
        self.reverse = [False for e in range(self.num_areas)]
        


        #WARNING: Hardcoded for testing
        self.reverse[0] = True
        #self.reverse[1] = True

        # ---------- Construct final path ----------
        path_list = [self.problem.initial_position]

        for i, i_area in enumerate(self.tour):
            # connect path
            path_file = self.folder + "connections\connection_" + str(i) +  ".csv"
            if self.verbose:
                print("connection file:", path_file)
            connection_path = np.genfromtxt(path_file, delimiter=',')

            if connection_path.ndim == 1:
                 m = connection_path.shape[0]
                 if m > 0:
                    path_list.append(connection_path)
            if connection_path.ndim == 2:
                for point in connection_path:
                    path_list.append(point) 
            
            # coverage path
            if All_paths[i_area]["len"]>0:
                path = All_paths[i_area]["path"]
                if self.reverse[i_area]:
                    path = path[::-1]
                for point in path:
                    path_list.append(point)


            if i == self.num_areas-1:
                path_file = self.folder + "connections\connection_" + str(i+1) +  ".csv"
                if self.verbose:
                    print("connection file:", path_file)
                connection_path = np.genfromtxt(path_file, delimiter=',')

                if connection_path.ndim == 1:
                    m = connection_path.shape[0]
                    if m > 0:
                        path_list.append(connection_path)
                if connection_path.ndim == 2:
                    for point in connection_path:
                        path_list.append(point) 


        path_list.append(self.problem.final_position)

        #if self.verbose:
        #    print("path:", path_list)

        path_list = np.array(path_list)
        #print(path_list)

        path = LineString(path_list)


        return path


        

