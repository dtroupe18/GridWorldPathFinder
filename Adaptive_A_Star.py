"""
A* path-finding algorithm
where successive rounds can only explore previously
explored cells thus resulting in fewer cells being explored every round

"""
import ConstructPath
import DisplayGridWorld
from heapq import heappop, heappush  # binary heap for open-list
import random


def manhattan_distance(a, b):  # heuristic function
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(grid_world, start, stop, g_scores, parents, rounds, previously_explored, display=False, adaptive=False):
    title = "Adaptive A Star HigherG"
    size = len(grid_world) - 1
    open_list = []
    complete_closed_list = []
    closed_list = set()
    max_distance = 101 ** 2

    if start not in g_scores:
        g_scores[start] = 0

    heappush(open_list, (0, 0, start, None))  # f, g, cell, parent

    while open_list:
        cell = heappop(open_list)
        previous_cell = cell[2]
        current_cell = cell[2]
        previous_cost = g_scores[current_cell]

        if current_cell == stop and rounds > 0:
            while rounds > 0:
                rounds -= 1
                complete_closed_list.append(cell)
                closed_list.add(current_cell)
                path = ConstructPath.construct_path_from_dict(parents, stop, start)
                s_goal = len(path)
                g_scores[1] = s_goal
                print("Rounds left:", rounds)
                print("Path length:", len(path))
                print("Number of Cells Explored:", len(closed_list))

                return a_star_search(grid_world, start, stop, g_scores, parents, rounds, closed_list, False, True)

        elif current_cell == stop and rounds == 0:
            complete_closed_list.append(cell)
            if display:
                path = ConstructPath.construct_path_from_dict(parents, stop, start)
                grid_world = ConstructPath.color_explored_cells(closed_list, grid_world, stop, start)
                grid_world = ConstructPath.color_shortest_path(path, grid_world, start)
                DisplayGridWorld.displayGridWorld(grid_world, title, False)
                return path, closed_list

            else:
                path = ConstructPath.construct_path_from_dict(parents, stop, start)
                return path, closed_list

        if current_cell in closed_list:
            continue  # ignore cells already evaluated

        if adaptive and current_cell not in previously_explored:
            continue  # ignore

        complete_closed_list.append(cell)
        closed_list.add(current_cell)

        # calculate f score for each valid neighbor
        x = current_cell[0]
        y = current_cell[1]

        if y > 0 and grid_world[x][y - 1] != 2 and (x, y - 1) not in closed_list:  # open cells are 1
            left = (x, y - 1)
            new_g_score = previous_cost + 1  # all moves cost 1

            if left in g_scores and g_scores[(x, y - 1)] < new_g_score:
                parent = parents[left]
            else:
                g_scores[left] = new_g_score
                parents[left] = previous_cell
                parent = previous_cell

            if adaptive:
                h_score = g_scores[1] - g_scores[left]
            else:
                h_score = manhattan_distance(left, stop)

            f_score = h_score * max_distance - g_scores[left]
            random_tie_breaker = random.randint(0, 100)
            heappush(open_list, (f_score, random_tie_breaker, left, parent))

        if x > 0 and grid_world[x - 1][y] != 2 and (x - 1, y) not in closed_list:
            up = (x - 1, y)
            new_g_score = previous_cost + 1

            if up in g_scores and g_scores[(x - 1, y)] < new_g_score:
                parent = parents[up]
            else:
                g_scores[up] = new_g_score
                parents[up] = previous_cell
                parent = previous_cell

            if adaptive:
                h_score = g_scores[1] - g_scores[up]
            else:
                h_score = manhattan_distance(up, stop)

            f_score = h_score * max_distance - g_scores[up]
            random_tie_breaker = random.randint(0, 100)
            heappush(open_list, (f_score, random_tie_breaker, up, parent))

        if y < size and grid_world[x][y + 1] != 2 and (x, y + 1) not in closed_list:
            right = (x, y + 1)
            new_g_score = previous_cost + 1

            if right in g_scores and g_scores[(x, y + 1)] < new_g_score:
                parent = parents[right]
            else:
                g_scores[right] = new_g_score
                parents[right] = previous_cell
                parent = previous_cell

            if adaptive:
                h_score = g_scores[1] - g_scores[right]
            else:
                h_score = manhattan_distance(right, stop)

            f_score = h_score * max_distance - g_scores[right]
            random_tie_breaker = random.randint(0, 100)
            heappush(open_list, (f_score, random_tie_breaker, right, parent))

        if x < size and grid_world[x + 1][y] != 2 and (x + 1, y) not in closed_list:
            down = (x + 1, y)
            new_g_score = previous_cost + 1

            if down in g_scores and g_scores[(x + 1, y)] < new_g_score:
                parent = parents[down]
            else:
                g_scores[down] = new_g_score
                parents[down] = previous_cell
                parent = previous_cell

            if adaptive:
                h_score = g_scores[1] - g_scores[down]
            else:
                h_score = manhattan_distance(down, stop)

            f_score = h_score * max_distance - g_scores[down]
            random_tie_breaker = random.randint(0, 100)
            heappush(open_list, (f_score, random_tie_breaker, down, parent))

    return ValueError("No Path Exists")
