from Tkinter import *
import random

#img = [[PhotoImage(file='./icon/block_%d.gif' % mat[x][y].val) for x in range(SizeX)] for y in range(SizeY)]

#for x in range(SizeX):
#	for y in range(SizeY):
#		Label(top, image=img[x][y]).grid(row=x, column=y)

#top.bind('Up', MoveUp(top, mat))
#top.bind('Down', MoveDown(top, mat))
#top.bind('Left', MoveLeft(top, mat))
#top.bind('Right',MoveRight(top, mat))

#top.mainloop()

#while 1:
#	pass


class _2048(Tk):
	def __init__(self,SizeX,SizeY):
		Tk.__init__(self)
		self.SizeX = SizeX
		self.SizeY = SizeY

		self.IsGameOver = False


		self.geometry('%dx%d' % ((self.SizeX+1)*100, (self.SizeY+1)*100))
		self.mat = [[0 for y in range(SizeY)] for x in range(SizeX)]
		self.gif = [[PhotoImage(file='./icon/block_%d.gif' % self.mat[x][y]) for x in range(SizeX)] for y in range(SizeY)]
		self.RandomCreate()
		self.Print()

	def MoveUp(self,e):
		print "Up"
		for x in range(self.SizeX):
			for y in range(self.SizeY):
				while self.Move(x,y,-1,0):
					pass
		[rest, maxval] = self.Count()
		if rest == 0:
			exit()
		#
		if maxval == 2048:
			exit()
		#
		self.RandomCreate()
		self.Print()

	def MoveDown(self,e):
		print "Down"
		for x in range(self.SizeX-1,-1,-1):
			for y in range(self.SizeY):
				while self.Move(x,y,+1,0):
					pass
		[rest, maxval] = self.Count()
		if rest == 0:
			exit()
		#
		if maxval == 2048:
			exit()
		#
		self.RandomCreate()
		self.Print()

	def MoveLeft(self,e):
		print "Left"
		for x in range(self.SizeX):
			for y in range(self.SizeY):
				while self.Move(x,y,0,-1):
					pass
		[rest, maxval] = self.Count()
		if rest == 0:
			exit()
		#
		if maxval == 2048:
			exit()
		#
		self.RandomCreate()
		self.Print()

	def MoveRight(self,e):
		print "Right"
		for x in range(self.SizeX):
			for y in range(self.SizeY-1,-1,-1):
				while self.Move(x,y,0,+1):
					pass
		[rest, maxval] = self.Count()
		if rest == 0:
			exit()
		#
		if maxval == 2048:
			exit()
		#
		self.RandomCreate()
		self.Print()

	def RandomCreate(self):
		[rest, maxval] = self.Count()
		t = random.randint(0,rest-1)
		for x in range(self.SizeX):
			for y in range(self.SizeY):
				if t < 0:	
					break
				elif t > 0: 	
					t -= 1
				else:		
					self.mat[x][y] = random.randint(0,1)*2+2
					t -= 1

	def Count(self):
		NumofNonzero = 0
		MaxVal = 0
		for x in range(self.SizeX):
			for y in range(self.SizeY):
				if self.mat[x][y] == 0: 
					NumofNonzero += 1
				if MaxVal < self.mat[x][y]:
					MaxVal = self.mat[x][y]
		return  [NumofNonzero, MaxVal]

	def Print(self):
	#clear
		for x in range(self.SizeX):
			for y in range(self.SizeY):
				a = self.grid_slaves(x, y)
				for tmp in a:
					tmp.destroy()
	#print mat
		self.gif = [[PhotoImage(file='./icon/block_%d.gif' % self.mat[x][y]) for x in range(self.SizeX)] for y in range(self.SizeY)]

		for x in range(self.SizeX):	
			for y in range(self.SizeY):
				Label(self, image=self.gif[x][y]).grid(row=y, column=x)
		for x in range(self.SizeX):
			print self.mat[x]

	def Move(self,x,y,dx,dy):
		if self.mat[x][y] == 0:
			return 0
		MergeFlag = 0
		if x+dx < 0 or x+dx >= self.SizeX:
			return 0
		if y+dy < 0 or y+dy >= self.SizeY:
			return 0
		if self.mat[x+dx][y+dy] == self.mat[x][y] or self.mat[x+dx][y+dy] == 0:
			MergeFlag = 1
		else:
			return 0
		self.mat[x+dx][y+dy] += self.mat[x][y]
		self.mat[x][y] = 0
		return 1
