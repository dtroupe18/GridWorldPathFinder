"""This script generates a grid-world using a list of lists that is then representing using pygame
the first randomly chosen spot is the start and colored green. The last cell to be selected is colored red.
The path would be from green to red (if possible)"""

import random


def generate_maze(size):

    maze = []
    unvisited = []

    for row in range(size):
        maze.append([])
        for column in range(size):
            maze[row].append(0)  # append a cell
            unvisited.append([row, column])

    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    maze[x][y] = 5  # unblocked - starting position
    s = (x, y)
    g = (None, None)
    unvisited.remove([x, y])  # visited

    while len(unvisited) > 0:

        check = []
        if y > 0 and maze[x][y - 1] == 0:
            check.append('L')
        if x > 0 and maze[x - 1][y] == 0:
            check.append('U')
        if y < size - 1 and maze[x][y + 1] == 0:
            check.append('R')
        if x < size - 1 and maze[x + 1][y] == 0:
            check.append('D')

        if len(check) > 0 and len(unvisited) > 1:
            direction_to_move = random.choice(check)  # move to a random cell

            if direction_to_move == 'L':
                y -= 1
                is_blocked = random.randint(0, 2)

                if is_blocked == 2:
                    maze[x][y] = 2
                    unvisited.remove([x, y])  # mark as visited

                else:
                    maze[x][y] = 1
                    unvisited.remove([x, y])  # mark as visited

            if direction_to_move == 'U':
                x -= 1
                is_blocked = random.randint(0, 2)

                if is_blocked == 2:
                    maze[x][y] = 2
                    unvisited.remove([x, y])  # mark as visited

                else:
                    maze[x][y] = 1
                    unvisited.remove([x, y])  # mark as visited

            if direction_to_move == 'R':
                y += 1
                is_blocked = random.randint(0, 2)

                if is_blocked == 2:
                    maze[x][y] = 2
                    unvisited.remove([x, y])  # mark as visited

                else:
                    maze[x][y] = 1
                    unvisited.remove([x, y])  # mark as visited

            if direction_to_move == 'D':
                x += 1
                is_blocked = random.randint(0, 2)

                if is_blocked == 2:
                    maze[x][y] = 2
                    unvisited.remove([x, y])  # mark as visited

                else:
                    maze[x][y] = 1
                    unvisited.remove([x, y])  # mark as visited

        else:
            if len(unvisited) > 1:
                random_move = random.choice(unvisited)  # move to a random unvisited cell
                x, y = random_move
                maze[x][y] = 1
                unvisited.remove([x, y])
            else:
                random_move = random.choice(unvisited)  # move to a random unvisited cell
                x, y = random_move
                maze[x][y] = 10  # goal
                g = (x, y)
                unvisited.remove([x, y])

    return maze, s, g


def generate_mazes(num_of_mazes, size_of_square_maze):
    mazes = {} # dictionary
    start = {}
    stop = {}
    for i in range(num_of_mazes):
        maze, s, g = generate_maze(size_of_square_maze)
        mazes[i] = maze
        start[i] = s
        stop[i] = g

    return mazes, start, stop
