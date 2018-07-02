import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()


# set up the window

# tuple = (x, y) where x = width of surface in pixels, y = height of surface in pixels 
windowSurface = pygame.display.set_mode((500, 400))
# Updates entire surface
pygame.display.update()

pygame.display.set_caption("Hello world!")

# uninitializes pygame
pygame.quit()





