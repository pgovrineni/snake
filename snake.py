import pygame
import time
import random

pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# define screen size
width, height = 600, 400

# initialize the display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# set the clock
clock = pygame.time.Clock()

# define the font
font_style = pygame.font.SysFont(None, 30)

# define the snake block size and speed
snake_block = 10
snake_speed = 15

# define the message to display on screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

# draw the snake on the screen
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

# the main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0       
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # create the food at random position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # check if snake is going out of bounds
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # update the snake's position
        x1 += x1_change
        y1 += y1_change
        display.fill(green)

        # draw the food on the screen
        pygame.draw.rect(display, blue, [foodx, foody, snake_block, snake_block])

        # append the snake's position to snake_List
        snake_Head = []
        snake_Head.append(x1)
        snake_Head
