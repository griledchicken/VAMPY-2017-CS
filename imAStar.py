import turtle as t
import random as r
def star(points):
	t.penup()
	t.right(180)
	t.forward(250)
	t.right(180)
	t.pendown()
	turn = 180 - (180 / points)
	m = points
	if(points % 2 == 0):
		m = 2 * points
	for i in range(m):
		dumb = r.randint(1, 250)
		t.color("light blue")
		t.speed(m)
		t.forward(500)
		t.right(turn)
	t.exitonclick()

star(251)














