import turtle

turtle.speed(0)

t = turtle.Turtle()

t.color('red')
t.begin_fill()
def hideturtle(x,y):
	t.penup()
	t.goto(x,y)
	t.pendown()

hideturtle(-75 , -75)
for _ in range(2):
	t.fd(150)
	t.circle(70,30)
	t.left(90-30)
	t.fd(100)
	t.circle(70,30)
	t.left(90-30)

t.end_fill()

hideturtle(0,-35)

t.color('white')
t.begin_fill()
t.left(90)

for _ in range(3):
	t.fd(75)
	t.right(360/3)

t.end_fill()

turtle.done()