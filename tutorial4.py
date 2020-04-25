import pygame

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

def snake():
    pygame.draw.rect(window, black, [x1, y1, block, block])

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

    # snake
    window.fill(blue)
    snake()
    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
