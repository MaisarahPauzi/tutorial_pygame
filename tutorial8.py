import pygame
import random

pygame.init()

# colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black= (0,0,0)
white = (255,255,255)

# window setup
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))

game_over = False

# snake/food block size 10 x 10
block = 10

# snake initial coordinate
x1 = 300
y1 = 200
# snake coordinate changes
x1_change = 0       
y1_change = 0

# initial food coordinate
food_x = round(random.randrange(0, window_width - block)/10)*10
food_y = round(random.randrange(0, window_height - block)/10)*10

# initial snake length
snake_length = 0
snake_list = []

# score text font setting
score_font = pygame.font.SysFont("comicsansms", 20)

def score_text(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    window.blit(value, [0, 0])

def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], block, block])

def food():
    pygame.draw.rect(window, green, [food_x, food_y, block, block])
    

while not game_over:
    # get event in the screen
    """
    pygame keyboard key constants (event.key)
    K_UP                  up arrow
    K_DOWN                down arrow
    K_RIGHT               right arrow
    K_LEFT                left arrow

    usage: pygame.K_UP
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10

            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
        
    x1 = x1 + x1_change
    y1 = y1 + y1_change

    # update window display
    window.fill(blue)

    # update snake
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    snake(snake_list)
    # update snake movement
    if len(snake_list) > snake_length:
        del snake_list[0]

    food()
    score_text(snake_length)
    pygame.display.update()
    # when snake eat food
    if x1 == food_x and y1 == food_y:
        food_x = round(random.randrange(0, window_width - block)/10)*10
        food_y = round(random.randrange(0, window_height - block)/10)*10
        food()
        snake_length = snake_length + 1

    #  when collide with border
    if (x1 >= window_width or x1 < 0) or (y1>= window_height or y1 < 0):
        game_over = True 

    pygame.time.delay(100)

pygame.quit()
