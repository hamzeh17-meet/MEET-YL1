import random
from meet import *
cells=[]
#cell1={"x":-20, "y":20, "radius":30, "dy":0.0032, "dx":0.003}
#cell2={"x":50, "y":-100, "radius":18, "dy":0.0002, "dx":-0.009}
#cell3={"x":30, "y":40, "radius":50, "dy":-0.01, "dx":0.004}
#z1=create_cell(cell1)
#cells.append(z1)
#z2=create_cell(cell2)
#cells.append(z2)
#z3=create_cell(cell3)
#cells.append(z3)
h=get_screen_height()
w=get_screen_width()
for i in range(200):
	cell={"x":get_random_x(), "y":get_random_y(), "radius":15, "dy":random.random(), "dx":random.random()}
	z=create_cell(cell)
	cells.append(z)
for h in cells:
	if (x>w,x<w*-1):
		"dx"=="dx"*-1
	if (y>h,y<h*-1):
		"dy"=="dy"*-1
		
while True:
	move_cells(cells)


