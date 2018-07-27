import pygame, sys
import time
import random
from pygame.locals import *

# set up pygame
pygame.init()
# User-defined colors
white = [255, 255, 255] #RGB -> Use RGB because computers have a backlight 
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 200, 0]
# set up the window, tuple = (x, y) where x = width of surface in pixels, y = height of surface in pixels 
displayWidth = 500
displayHeight = 400
windowSurface = pygame.display.set_mode((displayWidth, displayHeight)) # returns a pygame surface object
pygame.display.set_caption("Slither")
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
def snake(snakeList, blockSize):
	for xAndYLoc in snakeList:
		pygame.draw.rect(windowSurface, green, [xAndYLoc[0], xAndYLoc[1], blockSize, blockSize])
def gameLoop():
	gameExit = False
	gameOver = False
	leadX = displayWidth / 2 # Changing this is better than changing FPS -> explain why
	leadY = displayHeight / 2
	# allows user to hold down arrow key and see directionality change
	leadXChange = 0
	leadYChange = 0
	appleX = random.randrange(0, displayWidth - blockSize, blockSize)
	appleY = random.randrange(0, displayHeight - blockSize, blockSize)
	while not gameExit:
		# Pygame knows the events to watch out for (not on onus of programmer). It's up to you to do the event handling
		while gameOver:
			windowSurface.fill(white)
			msgToScreen("Game Over, press C to play again or Q to quit", red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					elif event.key == pygame.K_c:
						gameLoop()
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
			gameOver = True
		leadX += leadXChange
		leadY += leadYChange
		windowSurface.fill(white) #cleans the slate
		pygame.draw.rect(windowSurface, red, [appleX, appleY, blockSize, blockSize])

		snakeList = []
		snakeHead = []
		snakeHead.append(leadX)
		snakeHead.append(leadY)
		snakeList.append(snakeHead)
		snake(snakeList, blockSize)
		pygame.display.update() # rendering the graphic is the most CPU intensive 
		# Detect apple collision
		if leadX == appleX and leadY == appleY:
			appleX = random.randrange(0, displayWidth - blockSize, blockSize)
			appleY = random.randrange(0, displayHeight - blockSize, blockSize)
		# specify FPS
		clock.tick(FPS)

	# TODO: Add another condition for where user loses the game, don't want to exit game entirely. 
	# uninitializes pygame
	pygame.quit()
	# Must have -> exits out of python
	quit()
gameLoop()

 



