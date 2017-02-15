"""
A* pathfinding algorithm
Manhattan distance is the heuristic
Agent can only move in the four cardinal directions
(No Diagonal moves)

"""


from heapq import heappop, heappush  # binary heap for open-list


def manhattan_distance(a, b):  # heuristic function
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(grid_world, start, stop):
    count = 0
    open_list = []
    closed_list = []
    heappush(open_list, (0, start))

    while open_list:

        count += 1
        # Move to the best cell
        current_cell = heappop(open_list)
        current_cell = current_cell[1]

        #  print("Should be x, y at start", current_cell)
        if current_cell == stop:
            closed_list.append(current_cell)
            return closed_list
        if current_cell in closed_list:
            continue # ignore cells already evaluated
        closed_list.append(current_cell)

        # calculate f score for each valid neighbor
        x = current_cell[0]
        y = current_cell[1]

        #  print("x = ", x)
        #  print("y = ", y)
        #  print("length of grid-world =", len(grid_world))

        if y > 0 and (grid_world[x][y - 1] == 1 or grid_world[x][y - 1] == 10): # open cells are 1
            left = (x, y - 1)
            heappush(open_list, ((manhattan_distance(left, stop) + 1), left))
            # grid_world[x][y - 1] = - 1  color the explored cells blue!

        if x > 0 and (grid_world[x - 1][y] == 1 or grid_world[x - 1][y] == 10):
            up = (x -1, y)
            heappush(open_list, ((manhattan_distance(up, stop) + 1), up))
            # grid_world[x - 1][y] = -1  color in the explored cells blue

        if y < len(grid_world) - 1 and (grid_world[x][y + 1] == 1 or grid_world[x][y + 1] == 10):
            right = (x, y + 1)
            heappush(open_list, ((manhattan_distance(right, stop) + 1), right))
            # grid_world[x][y + 1] = -1  color the explored cells blue

        if x < len(grid_world) - 1 and (grid_world[x + 1][y] == 1 or grid_world[x + 1][y] == 10):
            down = (x + 1, y)
            heappush(open_list, ((manhattan_distance(down, stop) + 1), down))
            # grid_world[x + 1][y] = -1  color the explored cells blue

    return closed_list













