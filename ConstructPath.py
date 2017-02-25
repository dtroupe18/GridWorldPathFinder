

def get_index_of_tuple(l, index, value):
    for pos,t in enumerate(l):
        if t[index] == value:
            return pos

    # Matches behavior of list.index
    raise ValueError("list.index(x):", value, "not in list")


def construct_path(complete_closed_list, goal, start):
    current = goal  # construct the path backwards
    current_index = get_index_of_tuple(complete_closed_list, 2, current)
    parent_tuple = complete_closed_list[current_index]
    parent = parent_tuple[3]
    path = [parent]

    while parent != start:
        current_index = get_index_of_tuple(complete_closed_list, 2, parent)
        parent_tuple = complete_closed_list[current_index]
        parent = parent_tuple[3]
        path.append(parent)

    return path


def construct_path_from_dict(parents, goal, start):
    how_you_know_its_fucked = len(parents)
    count = 1
    current = goal
    parent = parents[current]
    path = [parent]

    while parent is not start:
        count += 1

        if parent not in parents:
            print("This is fucked")
        if parent == start:
            print("This is fucked 2")
        if count > how_you_know_its_fucked:
            print("problem parent", parent)
            break

        temp = parent
        parent = parents[temp]
        path.append(parent)

    return path




def color_explored_cells(closed_list, maze, start, goal):
    #  copy = list(maze)
    for cell in closed_list:
        if cell is not start and cell is not goal:
            x = cell[0]
            y = cell[1]
            maze[x][y] = 7
    return maze


def color_shortest_path(path, maze, start):
    #  copy = list(maze)
    for cell in path:
        if cell is not start:
            x = cell[0]
            y = cell[1]
            maze[x][y] = - 1
    return maze
