import DisplayGridWorld
import GenerateGridWorld
import A_Star_PathFinder

# takes about 90 seconds to generate the mazes
all_mazes, start, stop = GenerateGridWorld.generate_mazes(1, 101)  # stored in a dictionary from 0 - 49

print("start = ", start[0])
print("stop = ", stop[0])
current_maze = all_mazes[0]
heuristic = A_Star_PathFinder.manhattan_distance(start[0], stop[0])
print("Manhattan Distance from start to stop = ", heuristic)

# Display grid-world before navigation
# DisplayGridWorld.displayGridWorld(current_maze)

result = A_Star_PathFinder.a_star_search(current_maze, start[0], stop[0])
print("total distance traveled", len(result))

print("Path")
for cell in result:
    print(cell)
    if cell != start[0]:
        x = cell[0]
        y = cell[1]
        current_maze[x][y] = -1  # color the optimal path blue

# Display grid-world with path
DisplayGridWorld.displayGridWorld(current_maze)