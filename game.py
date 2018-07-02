import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()


# set up the window

# tuple = (x, y) where x = width of surface in pixels, y = height of surface in pixels 
windowSurface = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Slither")
# Updates entire surface
pygame.display.update()

gameExit = False
while not gameExit:
	# Pygame knows the events to watch out for (not on onus of programmer). It's up to you to do the event handling
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			gameExit = True
		


# uninitializes pygame
pygame.quit()
# Must have -> exits out of python
quit()





