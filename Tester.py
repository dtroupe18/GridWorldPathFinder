import DisplayGridWorld
import GenerateGridWorld
import A_Star_PathFinder
import A_Star_LowerG
import ConstructPath
import A_Star_HigherG

# takes about 90 seconds to generate the mazes
all_mazes, start, stop = GenerateGridWorld.generate_mazes(1, 101)  # stored in a dictionary from 0 - 49

print("start = ", start[0])
print("stop = ", stop[0])
current_maze = all_mazes[0]
copy_of_current_maze = list(current_maze)

heuristic = A_Star_PathFinder.manhattan_distance(start[0], stop[0])
print("Manhattan Distance from start to stop = ", heuristic)

cell_tuples, explored_cells = A_Star_LowerG.a_star_search(current_maze, start[0], stop[0])

print("cells explored", len(explored_cells))


# for cell in explored_cells:
#     if cell is not start[0] and stop[0]:
#         x = cell[0]
#         y = cell[1]
#         current_maze[x][y] = 7


#  DisplayGridWorld.displayGridWorld(current_maze) # display the cells that were explored

path = ConstructPath.construct_path(cell_tuples, stop[0], start[0])
current_maze = ConstructPath.color_explored_cells(explored_cells, current_maze, start[0], stop[0])
current_maze = ConstructPath.color_shortest_path(path, current_maze, start[0])

print(path)
print(len(path))

# for cell in path:
#     if cell is not start[0]:
#         x = cell[0]
#         y = cell[1]
#         copy_of_current_maze[x][y] = 7

DisplayGridWorld.displayGridWorld(copy_of_current_maze)  # display the shortest path

ccl, open_cells = A_Star_HigherG.a_star_search(copy_of_current_maze, start[0], stop[0])
DisplayGridWorld.displayGridWorld(copy_of_current_maze)

# they are comparing the same maze.... Fix this