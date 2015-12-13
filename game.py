import meet

import random
cells=[]
cells_nums=0
colors=['yellow','blue','red','green','orange','pink','purple']
while cells_nums<30:
	balls={'radius':random.randint(0,40),'x':random.randint(-100,150),'y':random.randint(-100,150),'dx':random.randint(-10,10),'dy':random.randint(-10,10)}
	cells_nums+=1
	circle=meet.create_cell(balls)
	cells.append(circle)

def check_x_border(cells):
	width=meet.get_screen_width()
	for cell in cells:
		if cell.xcor()>width or cell.xcor()<-width:
			h1=cell.get_dx()
			cell.set_dx(-h1)
def check_y_border(cells):
	height=meet.get_screen_height() 
	for cell in cells:
		if cell.ycor()>height or cell.ycor()<-height:
			h2=cell.get_dy()
			cell.set_dy(-h2)
		
while True:
	def move_cell(cell):
		'x' = cell.xcor()
		'dx' = cell.get_dx()
		'y' = cell.ycor()
		'dy' = cell.get_dy()
		'r' = cell.get_radius()
		cell.goto(x+dx,y+dy-r)
		cell.begin_fill()
		cell.pd()
		cell.circle(cell.get_radius())
		cell.penup()
		cell.end_fill()
		x = cell.xcor()
		dx = cell.get_dx()
		y = cell.ycor()
		dy = cell.get_dy()
		r = cell.get_radius()
		cell.goto(x+dx,y+dy+r)

	


