import GenerateGridWorld
import A_Star_PathFinder
import A_Star_LowerG
import A_Star_HigherG
import copy

# takes about 90 seconds to generate the mazes
all_mazes, start, stop = GenerateGridWorld.generate_mazes(1, 101)  # stored in a dictionary from 0 - 49
current_maze = all_mazes[0]
copy_of_current_maze = copy.deepcopy(current_maze)
backward_maze = copy.deepcopy(current_maze)
backward_maze2 = copy.deepcopy(current_maze)
heuristic = A_Star_PathFinder.manhattan_distance(start[0], stop[0])

path, explored_cells = A_Star_LowerG.a_star_search(current_maze, start[0], stop[0])
path2, explored_cells2 = A_Star_HigherG.a_star_search(copy_of_current_maze, start[0], stop[0])

reverse_path, reverse_explored = A_Star_LowerG.a_star_search(backward_maze, start[0], stop[0], True)
reverse_path2, reverse_explored2 = A_Star_HigherG.a_star_search(backward_maze2, start[0], stop[0], True)


print("Start = ", start[0])
print("Stop = ", stop[0])
print("Manhattan Distance from start to stop = ", heuristic)
print("Length of LowerG path =", len(path))
print("Length of HigherG path=", len(path2))
print("Length of reverse LowerG path =", len(reverse_path))
print("Length of reverse HigherG path=", len(reverse_path2))
print("Number of explored cells LowerG =", len(explored_cells))
print("Number of explored cells HigherG =", len(explored_cells2))
print("Number of explored cells reverse LowerG =", len(reverse_explored))
print("Number of explored cells reverse HigherG =", len(reverse_explored2))
