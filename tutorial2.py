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

    pygame.display.update()

pygame.quit()
quit()
