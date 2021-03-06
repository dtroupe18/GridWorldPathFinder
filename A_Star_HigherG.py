"""
A* path-finding algorithm
Manhattan distance is the heuristic
Agent can only move in the four cardinal directions
(No Diagonal moves) tie breaking favors cells with
a higher g cost.

The f score is already designed to favor cells with a larger g score
so the second value in the cell tuples is randomly generated to
further break ties.

Algorithm can be ran forward or backward

"""
import ConstructPath
import DisplayGridWorld
from heapq import heappop, heappush  # binary heap for open-list
import random


def manhattan_distance(a, b):  # heuristic function
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(grid_world, start, stop, display=False, reverse=False):
    if reverse:
        title = "Reverse A Star HigherG"
        start, stop = stop, start
    else:
        title = "A Star HigherG"

    size = len(grid_world) - 1
    open_list = []
    complete_closed_list = []
    closed_list = set()
    g_scores = {}
    parents = {}
    heappush(open_list, (0, 0, start, None))  # f, random, cell, parent
    max_distance = 101 ** 2
    g_scores[start] = 0

    while open_list:
        # Move to the best cell
        cell = heappop(open_list)
        # previous_cost = cell[1]
        # previous_cell = cell[2]
        current_cell = cell[2]
        previous_cost = g_scores[current_cell]

        if current_cell == stop:
            complete_closed_list.append(cell)
            if display:
                path = ConstructPath.construct_path(complete_closed_list, stop, start)
                grid_world = ConstructPath.color_explored_cells(closed_list, grid_world, stop, start)
                grid_world = ConstructPath.color_shortest_path(path, grid_world, start)
                DisplayGridWorld.displayGridWorld(grid_world, title, reverse)
                return path, closed_list

            else:
                path = ConstructPath.construct_path(complete_closed_list, stop, start)
                return path, closed_list
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
            new_g_score = previous_cost + 1  # all moves cost 1

            if left in g_scores and g_scores[(x, y - 1)] < new_g_score:
                    parent = parents[left]
            else:
                g_scores[left] = new_g_score
                parents[left] = current_cell
                parent = current_cell

            random_tie_breaker = random.randint(0, 100)
            f_score = manhattan_distance(left, stop) * max_distance - g_scores[left]  # f(n) = g(n) + h(n)
            heappush(open_list, (f_score, random_tie_breaker, left, parent))

        if x > 0 and grid_world[x - 1][y] != 2 and (x - 1, y) not in closed_list:
            up = (x - 1, y)
            new_g_score = previous_cost + 1

            if up in g_scores and g_scores[(x - 1, y)] < new_g_score:
                    parent = parents[up]
            else:
                g_scores[up] = new_g_score
                parents[up] = current_cell
                parent = current_cell

            random_tie_breaker = random.randint(0, 100)
            f_score = manhattan_distance(up, stop) * max_distance - g_scores[up]  # f(n) = g(n) + h(n)
            heappush(open_list, (f_score, random_tie_breaker, up, parent))

        if y < size and grid_world[x][y + 1] != 2 and (x, y + 1) not in closed_list:
            right = (x, y + 1)
            new_g_score = previous_cost + 1

            if right in g_scores and g_scores[(x, y + 1)] < new_g_score:
                    parent = parents[right]
            else:
                g_scores[right] = new_g_score
                parents[right] = current_cell
                parent = current_cell

            random_tie_breaker = random.randint(0, 100)
            f_score = manhattan_distance(right, stop) * max_distance - g_scores[right]  # f(n)  g(n) + h(n)
            heappush(open_list, (f_score, random_tie_breaker, right, parent))

        if x < size and grid_world[x + 1][y] != 2 and (x + 1, y) not in closed_list:
            down = (x + 1, y)
            new_g_score = previous_cost + 1

            if down in g_scores and g_scores[(x + 1, y)] < new_g_score:
                    parent = parents[down]
            else:
                g_scores[down] = new_g_score
                parents[down] = current_cell
                parent = current_cell

            random_tie_breaker = random.randint(0, 100)
            f_score = manhattan_distance(down, stop) * max_distance - g_scores[down]  # f(n)  g(n) + h(n)
            heappush(open_list, (f_score, random_tie_breaker, down, parent))

    return ValueError("No Path Exists")
