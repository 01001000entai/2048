#Main

from Tkinter import *
import Init
import Print
import Block
import Move

top = Tk();
top.geometry('%dx%d' % (SizeX*100, SizeY*100)
mat = Init()

Print(top,mat)

top.bind('Up', MoveUp(mat))
top.bind('Down', MoveDown(mat))
top.bind('Left', MoveLeft(mat))
top.bind('Right',MoveRight(mat))

