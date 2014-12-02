#Main

from Tkinter import *
import Init
import Print
import Block
import Move

top = Tk();
top.geometry('%dx%d' % (SizeX*100, SizeY*100)

Init(mat)

Print(top,mat)

top.bind('Up', MoveUp)
top.bind('Down', MoveDown)
top.bind('Left', MoveLeft)
top.bind('Right',MoveRight)

