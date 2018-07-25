import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
# User-defined colors
white = [255, 255, 255] #RGB -> Use RGB because computers have a backlight 
black = [0, 0, 0]
red = [255, 0, 0]

gameExit = False
# set up the window, tuple = (x, y) where x = width of surface in pixels, y = height of surface in pixels 
windowSurface = pygame.display.set_mode((500, 400)) # returns a pygame surface object
pygame.display.set_caption("Slither")
# Updates entire surface
leadX = 200 # Changing this is better than changing FPS -> explain why
leadY = 200
# allows user to hold down arrow key and see directionality change
leadXChange = 0
leadYChange = 0
clock = pygame.time.Clock()
# this while loop runs every frame
while not gameExit:
	# Pygame knows the events to watch out for (not on onus of programmer). It's up to you to do the event handling
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				leadXChange -= 10
			if event.key == pygame.K_RIGHT:
				leadXChange += 10
			if event.key == pygame.K_UP:
				leadYChange -= 10
			if event.key == pygame.K_DOWN:
				leadYChange += 10
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				leadXChange = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				leadYChange = 0
	leadX += leadXChange
	leadY += leadYChange
	windowSurface.fill(white) #cleans the slate
	pygame.draw.rect(windowSurface, black, [leadX, leadY, 10, 10]) # parameters = where we want to draw it, the color, and the coordinates
	pygame.display.update() # rendering the graphic is the most CPU intensive 
	# specify FPS
	clock.tick(10)

# TODO: Add another condition for where user loses the game, don't want to exit game entirely. 
		


# uninitializes pygame
pygame.quit()
# Must have -> exits out of python
quit()





