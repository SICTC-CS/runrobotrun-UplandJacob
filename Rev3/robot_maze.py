import turtle as t
import time

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move(n=1):
	for _ in range(n):
		robot.dot(10)
		robot.fd(50)

def turn(rt=False):
	robot.speed(0)
	robot.lt(-90 if rt else 90)
	robot.speed(2)

def turn_left():
	turn()
def turn_right():
	turn(True)

#----- init screen
wn = t.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "assets/robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = t.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

while True:
	for maze in range(1, 4+1):
		wn.bgpic(f"assets/maze{maze}.png")
		match maze:
			case 1:
				move(4)
				turn_right()
				move(4)
			case 2:
				move(3)
				turn_right()
				move(2)
			case 3:
				for i in range(8):
					move()
					if i % 2:
						turn_left()
					else:
						turn_right()
					if i == 4:
						robot.pencolor("red")
			case 4:
				for i in range(4):
					turn(i in [0, 3])
					move(2 if i % 2 else 1)
				turn_right()
				move(4)
				for i in range(4):
					turn(i in [0, 1])
					move(1 if i % 2 else 2)
		time.sleep(1)
		# reset
		robot.clear()
		robot.pencolor("darkorchid")
		robot.goto(startx, starty)
		robot.setheading(90)
