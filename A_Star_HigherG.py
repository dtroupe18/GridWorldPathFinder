"""
A* path-finding algorithm
Manhattan distance is the heuristic
Agent can only move in the four cardinal directions
(No Diagonal moves) tie breaking favors cells with
a higher g cost.

"""

from heapq import heappop, heappush  # binary heap for open-list


def manhattan_distance(a, b):  # heuristic function
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)


def get_neighbors(cell, grid_world):
    x = cell[0]
    y = cell[1]

    check = []
    if y > 0 and grid_world[x][y - 1] == 0:
        check.append((x, y - 1))
    if x > 0 and grid_world[x - 1][y] == 0:
        check.append((x - 1, y))
    if y < len(grid_world) - 1 and grid_world[x][y + 1] == 0:
        check.append((x, y + 1))
    if x < len(grid_world) - 1 and grid_world[x + 1][y] == 0:
        check.append((x + 1, y))

    return check


def get_f_score(initial_f, g_score):
    return ((101 ** 2) * initial_f) - (-1 * g_score)


def a_star_search(grid_world, start, stop):
    size = len(grid_world) - 1
    open_list = []
    complete_closed_list = []
    closed_list = set()
    g_scores = {}
    heappush(open_list, (0, 0, start, None))  # f, g, cell, parent
    max_distance = 101 ** 2

    while open_list:
        # Move to the best cell
        cell = heappop(open_list)
        previous_cost = cell[1]
        previous_cell = cell[2]
        current_cell = cell[2]

        if current_cell == stop:
            complete_closed_list.append(cell)
            return complete_closed_list, closed_list
            # returns a list of all explored cells in format (f, g, (x, y) parent)
        if current_cell in closed_list:
            continue  # ignore cells already evaluated
        complete_closed_list.append(cell)
        closed_list.add(current_cell)

        # calculate f score for each valid neighbor
        x = current_cell[0]
        y = current_cell[1]

        # only cells in the open list so they have a g score?
        if y > 0 and grid_world[x][y - 1] != 2 and (x, y - 1) not in closed_list:  # open cells are 1
            left = (x, y - 1)
            new_g_score = previous_cost + 1
            if left in g_scores:
                if g_scores[(x, y - 1)] > new_g_score:
                    g_scores[(x, y - 1)] = new_g_score
            else:
                g_scores[left] = new_g_score

            f_score = manhattan_distance(left, stop) * max_distance  - g_scores[left]  # f(n) = g(n) + h(n)
            heappush(open_list, (f_score, g_scores[left], left, previous_cell))

        if x > 0 and grid_world[x - 1][y] != 2 and (x - 1, y) not in closed_list:
            up = (x - 1, y)
            new_g_score = previous_cost + 1
            if up in g_scores:
                if g_scores[up] > new_g_score:
                    g_scores[up] = new_g_score
            else:
                g_scores[up] = new_g_score

            f_score = manhattan_distance(up, stop) * max_distance - g_scores[up]  # f(n) = g(n) + h(n)
            heappush(open_list, (f_score, g_scores[up], up, previous_cell))

        if y < size and grid_world[x][y + 1] != 2 and (x, y + 1) not in closed_list:
            right = (x, y + 1)
            new_g_score = previous_cost + 1
            if right in g_scores:
                if g_scores[right] > new_g_score:
                    g_scores[right] = new_g_score
            else:
                g_scores[right] = new_g_score

            f_score = manhattan_distance(right, stop) * max_distance - g_scores[right]  # f(n)  g(n) + h(n)
            heappush(open_list, (f_score, g_scores[right], right, previous_cell))

        if x < size and grid_world[x + 1][y] != 2 and (x + 1, y) not in closed_list:
            down = (x + 1, y)
            new_g_score = previous_cost + 1
            if down in g_scores:
                if g_scores[down] > new_g_score:
                    g_scores[down] = new_g_score
            else:
                g_scores[down] = new_g_score

            f_score = manhattan_distance(down, stop) * max_distance - g_scores[down]  # f(n)  g(n) + h(n)
            heappush(open_list, (f_score, g_scores[down], down, previous_cell))

    return ValueError("No Path Exists")
