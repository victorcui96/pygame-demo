import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

white = [255, 255, 255] #RGB -> Use RGB because computers have a backlight 
black = [0, 0, 0]
red = [255, 0, 0]

# set up the window

# tuple = (x, y) where x = width of surface in pixels, y = height of surface in pixels 
windowSurface = pygame.display.set_mode((500, 400)) # returns a pygame surface object
pygame.display.set_caption("Slither")
# Updates entire surface

gameExit = False
while not gameExit:
	# Pygame knows the events to watch out for (not on onus of programmer). It's up to you to do the event handling
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			gameExit = True
	windowSurface.fill(white)
	pygame.display.update() # rendering the graphic is the most CPU intensive 


# TODO: Add another condition for where user loses the game, don't want to exit game entirely. 
		


# uninitializes pygame
pygame.quit()
# Must have -> exits out of python
quit()





