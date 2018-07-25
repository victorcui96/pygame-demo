import pygame, sys
import time
from pygame.locals import *

# set up pygame
pygame.init()
# User-defined colors
white = [255, 255, 255] #RGB -> Use RGB because computers have a backlight 
black = [0, 0, 0]
red = [255, 0, 0]

gameExit = False
# set up the window, tuple = (x, y) where x = width of surface in pixels, y = height of surface in pixels 
displayWidth = 500
displayHeight = 400
windowSurface = pygame.display.set_mode((displayWidth, displayHeight)) # returns a pygame surface object
pygame.display.set_caption("Slither")
# Updates entire surface
leadX = displayWidth / 2 # Changing this is better than changing FPS -> explain why
leadY = displayHeight / 2
# allows user to hold down arrow key and see directionality change
leadXChange = 0
leadYChange = 0
clock = pygame.time.Clock()
blockSize = 10
FPS = 20
# font object, 2nd parameter = font size
font = pygame.font.SysFont(None, 25)
# this while loop runs every frame
def msgToScreen(msg, color):
	screenText = font.render(msg, True, color)
	# put font on display
	windowSurface.blit(screenText, [displayWidth / 2, displayHeight / 2])
while not gameExit:
	# Pygame knows the events to watch out for (not on onus of programmer). It's up to you to do the event handling
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				leadXChange -= blockSize
			elif event.key == pygame.K_RIGHT:
				leadXChange += blockSize
			elif event.key == pygame.K_UP:
				leadYChange -= blockSize
			elif event.key == pygame.K_DOWN:
				leadYChange += blockSize
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				leadXChange = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				leadYChange = 0
	if leadX >= displayWidth or leadX < 0 or leadY < 0 or leadY >= displayHeight:
		gameExit = True
	leadX += leadXChange
	leadY += leadYChange
	windowSurface.fill(white) #cleans the slate
	pygame.draw.rect(windowSurface, black, [leadX, leadY, blockSize, blockSize]) # parameters = where we want to draw it, the color, and the coordinates
	pygame.display.update() # rendering the graphic is the most CPU intensive 
	# specify FPS
	clock.tick(FPS)

# TODO: Add another condition for where user loses the game, don't want to exit game entirely. 
msgToScreen("You Lose", red)
pygame.display.update()
time.sleep(2)
# uninitializes pygame
pygame.quit()
# Must have -> exits out of python
quit()





