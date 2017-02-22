# used to draw grid worlds
import pygame


def displayGridWorld(maze, title, reverse=False):
    # define colors
    black = (0, 0, 0) # blocked
    white = (255, 255, 255) # unblocked
    green = (0, 255, 0) # start
    red = (255, 0, 0) # end
    blue =(0, 0, 255) # explored cells
    orange = (255, 153, 0)  # shortest path

    # set width and height of window
    size = [850, 850]
    screen = pygame.display.set_mode(size)

    # set height, width, and margin for squares
    width = 7
    height = 7
    margin = 1

    # initialize the game engine
    pygame.init()
    pygame.display.set_caption(title)

    # Loop until user closes the window
    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():  # user did something
            if event.type == pygame.QUIT:  # user clicked close
                done = True

        # all event processing

        # all game logic

        # code to draw
        screen.fill(black)

        # draw the grid
        for row in range(len(maze)):
            for column in range(len(maze)):
                # color = white
                if maze[row][column] == 1:
                    color = white
                elif maze[row][column] == 2:
                    color = black
                elif maze[row][column] == 5:
                    if reverse:
                        color = red
                    else:
                        color = green
                elif maze[row][column] == 10:
                    if reverse:
                        color = green
                    else:
                        color = red
                elif maze[row][column] == 7:
                    color = blue  # explored cells
                else:
                    color = orange  # shortest path

                pygame.draw.rect(screen, color, [(margin + width) * column + margin,
                                                 (margin + height) * row + margin,
                                                 width, height])

        # 20 frames per second
        clock.tick(20)
        pygame.display.flip()
    pygame.quit()
