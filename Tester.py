import A_Star_LowerG
import A_Star_HigherG
import Adaptive_A_Star
import copy
import pickle
import time

# Load Data

with open('all_mazes.pickle', 'rb') as handle:
    all_mazes = pickle.load(handle)

with open('start_locations.pickle', 'rb') as handle:
    start = pickle.load(handle)

with open('goal_locations.pickle', 'rb') as handle:
    stop = pickle.load(handle)

d ={}
p = {}
x = 19  # maze number
current_maze = all_mazes[x]
copy_of_current_maze = copy.deepcopy(current_maze)
backward_maze = copy.deepcopy(current_maze)
backward_maze2 = copy.deepcopy(current_maze)
adaptive_maze = copy.deepcopy(current_maze)
heuristic = A_Star_LowerG.manhattan_distance(start[x], stop[x])

lowerg_time = time.time()
path, explored_cells = A_Star_LowerG.a_star_search(current_maze, start[x], stop[x], True)
lowerg_end = time.time()

start_time = time.time()
path2, explored_cells2 = A_Star_HigherG.a_star_search(copy_of_current_maze, start[x], stop[x], True)
end_time = time.time()

reverse_lowerg_time = time.time()
reverse_path, reverse_explored = A_Star_LowerG.a_star_search(backward_maze, start[x], stop[x], True, True)
reverse_reverse_lowerg_end = time.time()

reverse_higherG = time.time()
reverse_path2, reverse_explored2 = A_Star_HigherG.a_star_search(backward_maze2, start[x], stop[x], True, True)
reverse_higherG_end = time.time()

adap_start = time.time()
adaptive_path, adaptive_explored = Adaptive_A_Star.a_star_search(adaptive_maze, start[x], stop[x], d, p, 3, False)
adap_end = time.time()

print("Start = ", start[0])
print("Stop = ", stop[0])
print("Manhattan Distance from start to stop = ", heuristic)
print("Length of LowerG path =", len(path))
print("Length of HigherG path=", len(path2))
print("Length of reverse LowerG path =", len(reverse_path))
print("Length of reverse HigherG path=", len(reverse_path2))
print("Length of Adaptive HigherG path=", len(adaptive_path))
print("Number of explored cells LowerG =", len(explored_cells))
print("Number of explored cells HigherG =", len(explored_cells2))
print("Number of explored cells reverse LowerG =", len(reverse_explored))
print("Number of explored cells reverse HigherG =", len(reverse_explored2))
print("Number of explored cells Adaptive A* =", len(adaptive_explored))
print("Lower G A* time               ", lowerg_end - lowerg_time)
print("Higher G A* time              ", end_time - start_time)
print("Adaptive A* time with 3 rounds", adap_end - adap_start)
print("Reverse Lower G A* time       ", reverse_reverse_lowerg_end - reverse_lowerg_time)
print("Reverse Higher G A* time      ", reverse_higherG_end - reverse_higherG)


