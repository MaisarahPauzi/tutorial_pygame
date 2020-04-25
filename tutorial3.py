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

def snake():
    pygame.draw.rect(window, black, [300, 200, 10, 10])

while not game_over:
    window.fill(blue)
    # snake
    snake()

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
                print('UP')
            elif event.key == pygame.K_DOWN:
                print('DOWN')
            elif event.key == pygame.K_RIGHT:
                print('RIGHT')
            elif event.key == pygame.K_LEFT:
                print('LEFT')
            

    pygame.display.update()

pygame.quit()
