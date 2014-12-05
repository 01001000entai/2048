#Main

from Tkinter import *
import _2048

top = _2048._2048(4,4)
		
#top.mat_gif = [[Label(self) for y in range(SizeY)] for x in range(SizeX)]
top.bind('<Key-Left>', top.MoveLeft)
top.bind('<Key-Right>', top.MoveRight)
top.bind('<Key-Up>', top.MoveUp)
top.bind('Key-Down', top.MoveDown)


#img = [[PhotoImage(file='./icon/block_%d.gif' % mat[x][y].val) for x in range(SizeX)] for y in range(SizeY)]

#for x in range(SizeX):
#	for y in range(SizeY):
#		Label(top, image=img[x][y]).grid(row=x, column=y)

#top.bind('Up', MoveUp(top, mat))
#top.bind('Down', MoveDown(top, mat))
#top.bind('Left', MoveLeft(top, mat))
#top.bind('Right',MoveRight(top, mat))

top.mainloop()

#while 1:
#	pass