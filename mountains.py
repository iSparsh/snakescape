import turtle
import random
def start(time):
	"""Starts the building process of a Mountain"""

	# Mountains

	print("\n\n🐍: Welcome to the Mountainsss! How many of these Mountainsss do you want?")
	try:
		num_mountains = int(input("> Choose between 1 and 10: "))
	except:
		num_mountains = random.randint(1, 10)
	if num_mountains not in range(1, 11):
		num_mountains = random.randint(1, 10)
	print(f"So the number of mountains that have formed are: {num_mountains}")
	
	# Trees

	print("\n🐍: How many of treesss do you desssire?")
	try:
		num_trees = int(input("> Choose between 1 and 10: "))
	except:
		num_trees = random.randint(1, 10)
	if num_trees not in range(1, 11):
		num_trees = random.randint(1, 10)
	print(f"So the number of trees that have been planted are: {num_trees}")
	
	# Drawing Begins
	draw(num_mountains, num_trees, time)

def draw(mountains, trees, time):
	"""Initiates the drawing process"""

	turtle.speed(0)
	turtle.bgcolor(time)

	# drawing grass
	turtle.penup()
	turtle.goto(-400, -100)
	turtle.pendown()
	turtle.color("limegreen")
	turtle.begin_fill()

	for i in range(2):
	    turtle.forward(800)
	    turtle.right(90)
	    turtle.forward(400)
	    turtle.right(90)

	turtle.end_fill()

	for _ in range(mountains):
		draw_mountain()

	if time == "darkblue": # it is night
		draw_sky_entity("moon")
	else:
		draw_sky_entity("sun")

	turtle.right(90)

	for _ in range(trees):
		draw_trees()
	
	turtle.done()

def draw_mountain():
	mountain_colors = ["gray", "dimgray", "brown"]
	turtle.penup()
	starting = random.randint(-410, 120)
	turtle.goto(starting, -100)
	turtle.pendown()
	turtle.color(mountain_colors[random.randint(0, 2)])
	turtle.begin_fill()
	for i in range(3):
		turtle.forward(300)
		turtle.left(120) 
	turtle.end_fill()

def draw_trees():
	tree_colors = ["forestgreen", "darkgreen", "green"]
	
	x_value = random.randint(-300, 100)
	y_value = random.randint(100, 300)
	turtle.penup()
	turtle.goto(x_value, -y_value)
	turtle.pendown()
	
	# Tree trunk
	turtle.color("saddlebrown")
	turtle.begin_fill()
	for i in range(2):
	    turtle.forward(40)
	    turtle.left(90)
	    turtle.forward(10)
	    turtle.left(90)
	turtle.end_fill()
    
    # Turn the turtle around
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(5)
    
    # Leaves on tree
	turtle.color(tree_colors[random.randint(0, 2)])
	turtle.begin_fill()
	turtle.circle(25)
	turtle.end_fill()
    
	turtle.right(90)

def draw_sky_entity(entity):
	turtle.penup()
	turtle.goto(-400, 100)
	turtle.pendown()
	if entity == "moon":
		turtle.color("white")
	else:
		turtle.color("yellow")
	turtle.begin_fill()
	turtle.circle(125)
	turtle.end_fill()