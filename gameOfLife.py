import pygame
import random
import time

HEIGHT = 480
WIDTH = 640
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

chance = float(input("How likely are random squares to be alive at first? "))
grid = []
for i in range(48):
	grid.append([])
	for j in range(64):
		if random.uniform(0, 1) < chance:
			grid[i].append(1)
		else:
			grid[i].append(0)

genx = []
for i in range(48):
	genx.append([])
	for j in range(64):
			genx[i].append(0)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Game of Life!")
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	for i in range(48):
		for j in range(64):
			xpos = j*10
			ypos = i*10
			cell = pygame.Rect(xpos, ypos, 10, 10)
			if grid[i][j] == 1:
				pygame.draw.rect(screen, BLACK, cell)
			else:
				pygame.draw.rect(screen, WHITE, cell)
	pygame.display.flip()
	pygame.display.update()
	time.sleep(1/30)

	for i in range(48):
		genx.append([])
		for j in range(64):
			n = 0
			above = (i+1) % 48
			below = (i-1) % 48
			left = (i+1) % 64
			right = (i-1) % 64
			n += grid[above][j]
			n += grid[below][j]
			n += grid[i][left]
			n += grid[i][right]
			n += grid[above][left]
			n += grid[above][right]
			n += grid[below][left]
			n += grid[below][right]
			if n < 2:
				genx[i][j] = 0
			elif n > 3:
				genx[i][j] = 0
			elif n == 3:
				genx[i][j] = 1
			else:
				genx[i][j] = grid[i][j] 
	grid = genx
	
		
