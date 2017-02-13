# used to draw grid worlds
import pygame


def displayGridWorld(maze):
    # define colors
    black = (0, 0, 0) # blocked
    white = (255, 255, 255) # unblocked
    green = (0, 255, 0) # start
    red = (255, 0, 0) # end
    blue =(0, 0, 255) # path color

    # set width and height of window
    size = [850, 850]
    screen = pygame.display.set_mode(size)

    # set height, width, and margin for squares
    width = 7
    height = 7
    margin = 1

    # initialize the game engine
    pygame.init()
    pygame.display.set_caption("Grid World")

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
                    color = green
                elif maze[row][column] == 10:
                    color = red
                else:
                    color = blue

                pygame.draw.rect(screen, color, [(margin + width) * column + margin,
                                                 (margin + height) * row + margin,
                                                 width, height])

        # 20 frames per second
        clock.tick(20)
        pygame.display.flip()
    pygame.quit()
