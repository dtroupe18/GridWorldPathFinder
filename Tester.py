import DisplayGridWorld
import GenerateGridWorld
import A_Star_PathFinder
import A_Star_LowerG
import ConstructPath
import A_Star_HigherG
import copy

# takes about 90 seconds to generate the mazes
all_mazes, start, stop = GenerateGridWorld.generate_mazes(1, 101)  # stored in a dictionary from 0 - 49
current_maze = all_mazes[0]
copy_of_current_maze = copy.deepcopy(current_maze)
heuristic = A_Star_PathFinder.manhattan_distance(start[0], stop[0])
cell_tuples, explored_cells = A_Star_LowerG.a_star_search(current_maze, start[0], stop[0])
path = ConstructPath.construct_path(cell_tuples, stop[0], start[0])
current_maze = ConstructPath.color_explored_cells(explored_cells, current_maze, start[0], stop[0])
current_maze = ConstructPath.color_shortest_path(path, current_maze, start[0])

# display the shortest path and explored cells with LowerG
DisplayGridWorld.displayGridWorld(current_maze)

cell_tuples2, explored_cells2 = A_Star_HigherG.a_star_search(copy_of_current_maze, start[0], stop[0])
path2 = ConstructPath.construct_path(cell_tuples2, stop[0], start[0])
copy_of_current_maze = ConstructPath.color_explored_cells(explored_cells2, copy_of_current_maze, start[0], stop[0])
copy_of_current_maze = ConstructPath.color_shortest_path(path2, copy_of_current_maze, start[0])
DisplayGridWorld.displayGridWorld(copy_of_current_maze)

print("Start = ", start[0])
print("Stop = ", stop[0])
print("Manhattan Distance from start to stop = ", heuristic)
print("Cells explored with LowerG", len(explored_cells))
print("Cells explored with HigherG", len(explored_cells2))
print("LowerG path", path)
print("HigherG path", path2)
print("Length of LowerG Path", len(path))
print("Length of HigherG Path", len(path2))

# they are comparing the same maze.... Fix this change copy of current maze