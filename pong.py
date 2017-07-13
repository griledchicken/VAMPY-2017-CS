import pygame
import time
import random

WIDTH = (640)
HEIGHT = (480)
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WAITING = 1
PLAYING = 2

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong!")

state = WAITING
state_time = time.time()

speed_lpaddle = 0
speed_rpaddle = 0
speed_ballx = 0
speed_bally = 0

paddle_w = 0.025*WIDTH
paddle_h = 10*paddle_w
ball_w = paddle_w
rect_lpaddle = pygame.Rect(0.05*WIDTH, HEIGHT/2 - WIDTH/2, paddle_w, paddle_h)
rect_rpaddle = pygame.Rect(0.9*WIDTH, HEIGHT/2 - WIDTH/2, paddle_w, paddle_h)
rect_ball = pygame.Rect(WIDTH/2 - ball_w/2, HEIGHT/2 - ball_w/2, ball_w, ball_w)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			speed_lpaddle = 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			speed_lpaddle = -2
		elif event.type == pygame.KEYUP and event.key == pygame.K_s:
			speed_lpaddle = 0
		elif event.type == pygame.KEYUP and event.key == pygame.K_w:
			speed_lpaddle = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			speed_rpaddle = -2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			speed_rpaddle = 2
		elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
			speed_rpaddle = 0
		elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			speed_rpaddle = 0

	rect_lpaddle.move_ip(0, speed_lpaddle)
	rect_rpaddle.move_ip(0, speed_rpaddle)
	if state == PLAYING:
		rect_ball.move_ip(speed_ball_x, speed_ball_y)
	elif state == WAITING:
		if time.time() - state_time >= 2:
			state = PLAYING
			state_time = time.time()
			speed_ball_x = 2*random.randint(0, 1) - 1
			speed_ball_y = 2*random.randint(-5, 5)
		
	if rect_ball.y <= 0:
		rect_ball.y = 0
		speed_ball_y = abs(speed_ball_y)
	elif rect_ball.y + rect_ball.h >= HEIGHT:
		rect_ball.y = HEIGHT - rect_ball.h
		speed_ball_y = -abs(speed_ball_y)

	if rect_lpaddle.x <= rect_ball.x and rect_ball.x <= rect_lpaddle.x + rect_lpaddle.w:
		if rect_lpaddle.y <= rect_ball.y and rect_ball.y <= rect_lpaddle.y + rect_lpaddle.h:
			rect_ball.x = rect_lpaddle.x - rect_ball.w
			speed_ball_x = abs(speed_ball_x)
			peed_ball_x = random.randint(-5, 5)
	
	elif rect_rpaddle.x <= rect_ball.x + rect_ball.w and rect_ball.x + rect_ball.w <= rect_rpaddle.x + rect_rpaddle.w:
		if rect_rpaddle.y - rect <= rect_ball.y and rect_ball.y <= rect_lpaddle.y + rect_lpaddle.h:
			rect_ball.x = rect_rpaddle.x - rect_ball.w
			speed_ball_x = abs(speed_ball_x)
			speed_ball_x = random.randint(-5, 5)

	if rect_ball.x + rect_ball.w < 0:
		state = WAITING
		state_time = time.time()	
		rect_ball.x = WIDTH/2 - rect_ball.w/2
		rect_ball.y = HIGHT/2 - rect_ball.h/2

	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, rect_lpaddle)
	pygame.draw.rect(screen, WHITE, rect_rpaddle)
	pygame.draw.rect(screen, WHITE, rect_ball)
	pygame.display.flip()

	time.sleep(1/100)
