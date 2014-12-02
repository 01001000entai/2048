#Use Tkinter to print

from Tkinter import *
import Init

def Print(top,mat):
	#clear
	for x in range(SizeX):
		for y in range(SizeY):
			a = top.grid_slaves(x, y)
			for tmp in a:
				tmp.destroy()
	#print mat
	for x in range(SizeX):
		for y in range(SizeY):
			img = PhotoImage(file='block_%d.gif' % mat[x][y].val)
			Label(top, image=img).grid(row=x, column=y)






