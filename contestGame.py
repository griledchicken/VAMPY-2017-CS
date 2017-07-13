import pygame
import time

SIZE = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREENa1 = (170, 255, 170)
GREENb1 = (85, 255, 85)
GREENa2 = (0, 85, 0)
GREENb2 = (0, 170, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello, World!")

square1 = pygame.Rect(640/2 - 250, 480/2 - 100/2, 100, 100)
square2 = pygame.Rect(640/2 + 150, 480/2 - 100/2, 100, 100)
directionx1 = 0
directiony1 = 0
directionx2 = 0
directiony2 = 0
state1 = 0
state2 = 0
dead1 = 0
dead2 = 0
timd1 = 0
timd2 = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			directionx1 = 2
			directiony1 = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			directionx1 = -2
			directiony1 = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			directiony1 = -2
			directionx1 = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			directiony1 = 2
			directionx1 = 0
		if event.type == pygame.KEYUP and event.key in [pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s]:
			directionx1 = 0
			directiony1 = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			directionx2 = 2
			directiony2 = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			directionx2 = -2
			directiony2 = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			directiony2 = -2
			directionx2 = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			directiony2 = 2
			directionx2 = 0
		elif event.type == pygame.KEYUP and event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
			directionx2 = 0
			directiony2 = 0
		if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			state1 = 1
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
			state1 = 2
		if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
			state2 = 1
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_k:
			state2 = 2
		if event.type == pygame.KEYUP and event.key in [pygame.K_q, pygame.K_e]:
			state1 = 0
		if event.type == pygame.KEYUP and event.key in [pygame.K_k, pygame.K_m]:
			state2 = 0
	screen.fill(GREEN)
	if pygame.Rect.colliderect(square1, square2) == True:
		if state1 == 2 and time.time() - timd2 > 1:
			if state2 != 1:
				dead2 += 1
				timd2 = time.time()
		elif state2 == 2 and time.time() - timd1 > 1:
			if state1 != 1:
				dead1 += 1
				timd1 = time.time()
	if dead1 == 3:
		state1 = 3
	if dead2 == 3:
		state1 = 3
	if state1 == 0 and dead1 == 0:
		pygame.draw.rect(screen, WHITE, square1)
	elif state1 == 0 and dead1 == 1:
		pygame.draw.rect(screen, GREENa1, square1)
	elif state1 == 0 and dead1 == 2:
		pygame.draw.rect(screen, GREENb1, square1)
	elif state1 == 1:
		pygame.draw.rect(screen, BLUE, square1)
	elif state1 == 2:
		pygame.draw.rect(screen, RED, square1)
	else:
		print("Plaer 2 wins!")
		pygame.quit()
		exit()
	if state2 == 0 and dead2 == 0:
		pygame.draw.rect(screen, BLACK, square2)
	elif state2 == 0 and dead2 == 1:
		pygame.draw.rect(screen, GREENa2, square2)
	elif state2 == 0 and dead2 == 2:
		pygame.draw.rect(screen, GREENb2, square2)
	elif state2 == 1:
		pygame.draw.rect(screen, BLUE, square2)
	elif state2 == 2:
		pygame.draw.rect(screen, RED, square2)
	else:
		print("Plaer 1 wins!")
		pygame.quit()
		exit()
				
	pygame.display.flip()

	time.sleep(1/300)

	square1 = square1.move(directionx1, directiony1)
	square2 = square2.move(directionx2, directiony2)
	if square1.x + square1.w + 10 >= SIZE[0]:
		directionx1 = 0
	elif square1.x - 10 <= 0:
		directionx1 = 0
	elif square1.y  - 10 <= 0:
		directiony1 = 0
	elif square1.y + square1.w + 10 >= SIZE[1]:
		directiony1 = 0
	elif square2.x + square2.w + 10 >= SIZE[0]:
		directionx2 = 0
	elif square2.x - 10 <= 0:
		directionx2 = 0
	elif square2.y  - 10 <= 0:
		directiony2 = 0
	elif square2.y + square2.w + 10 >= SIZE[1]:
		directiony2 = 0
