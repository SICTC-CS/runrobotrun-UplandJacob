#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "assets/robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
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
	for maze in range(1, 4):
		wn.bgpic(f"assets/maze{maze}.png")
		match maze:
			case 1:
				for _ in range(4):
					move()
				for _ in range(3):
					turn_left()
				for _ in range(4):
					move()
			case 2:
				for _ in range(3):
					move()
				for _ in range(3):
					turn_left()
				for _ in range(2):
					move()
			case 3:
				for i in range(8):
					move()
					for _ in range(3 if not i % 2 else 1): # 1 for left, 3 for right, alternating
						turn_left()
					if i == 4:
						robot.pencolor("red")
		# reset
		robot.clear()
		robot.pencolor("darkorchid")
		robot.goto(startx, starty)
		robot.setheading(90)
