import A_Star_LowerG
import A_Star_HigherG
import Adaptive_A_Star
import pickle
import time

# Load Data

with open('all_mazes.pickle', 'rb') as handle:
    all_mazes = pickle.load(handle)

with open('start_locations.pickle', 'rb') as handle:
    start = pickle.load(handle)

with open('goal_locations.pickle', 'rb') as handle:
    stop = pickle.load(handle)

lowerG_Average_Cells_Explored = 0
lowerG_Average_Time = 0
higherG_Average_Cells_Explored = 0
higherG_Average_Time = 0
adaptiveHigherG_Average_Cells_Explored = 0
adaptiveHigherG_Average_Time = 0

d ={}
p = {}


# lower_time = time.time()
# for x in range(0, 50):
#     current_maze = all_mazes[x]
#     path, explored_cells = A_Star_LowerG.a_star_search(current_maze, start[x], stop[x])
# lower_time_end = time.time()

higher_time = time.time()
for x in range(0, 50):
    current_maze = all_mazes[x]
    path, explored_cells2 = A_Star_HigherG.a_star_search(current_maze, start[x], stop[x])
higher_time_end = time.time()

# adapt_time = time.time()
# for x in range(0, 6):
#     current_maze = all_mazes[x]
#     path, adaptive_explored = Adaptive_A_Star.a_star_search(current_maze, start[x], stop[x], d, p, 3, False)
# adapt_time_end = time.time()
# time = (adapt_time_end - adapt_time) * 10
# time /= 50


# print("Average time taken for lower G:    ", (lower_time_end - lower_time) / 50)
print("Average time taken for Higher G:   ", (higher_time_end - higher_time) / 50)
print("Average time taken for Adaptive A*:", time)