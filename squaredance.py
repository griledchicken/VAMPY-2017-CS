import pygame
import time

SIZE = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello, World!")

square = pygame.Rect(640/2 - 100/2, 480/2 - 100/2, 100, 100)
directionx = 0
directiony = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			directionx = 2
			directiony = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			directionx = -2
			directiony = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			directiony = -2
			directionx = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			directiony = 2
			directionx = 0
		elif event.type == pygame.KEYUP:
			directionx = 0
			directiony = 0
	screen.fill(GREEN)
	pygame.draw.rect(screen, BLUE, square)
	pygame.display.flip()

	time.sleep(1/300)

	square = square.move(directionx, directiony)
	if square.x + square.w + 10 >= SIZE[0]:
		directionx = 0
	elif square.x - 10 <= 0:
		directionx = 0
	elif square.y  - 10 <= 0:
		directiony = 0
	elif square.y + square.w + 10 >= SIZE[1]:
		directiony = 0
