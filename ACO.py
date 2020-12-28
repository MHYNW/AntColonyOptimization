"""

Ant Colony Optimization for UAVs

Author: MHYNW
        #https://github.com/MHYNW
        #phdcarrot@gmail.com

"""

import sys
sys.path.append("/Users/mhyyyunwoo/Workspace/AntColonyOptimization/ant-colony-optimization")
import ant_colony_prac
import math
from enum import Enum
import numpy as np

# given some nodes, and some locations...
test_nodes = {0: (0, 7), 1: (3, 9), 2: (12, 4), 3: (14, 11), 4: (8, 11), 5: (15, 6), 6: (6, 15), 7: (15, 9), 8: (12, 10), 9: (10, 7)}

# and a function to get distance between nodes
def distance(start, end):
	x_distance = abs(start[0] - end[0])
	y_distance = abs(start[1] - end[1])
	
	# c = sqrt(a^2 + b^2)
	import math
	return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

# we can make a colony of ants
colony = ant_colony_prac.ant_colony(test_nodes, distance)

# that will find the optimal solution with ACO
answer = colony.mainloop()

print(answer)
