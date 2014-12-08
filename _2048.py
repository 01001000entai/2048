from Tkinter import *
from SimpleDialog import *
import random

class _2048(Tk):
	def __init__(self,SizeX,SizeY):
		Tk.__init__(self)
		
		self.SizeX = SizeX
		self.SizeY = SizeY
		self.Point = 0
		self.IsGameOver = False
		self.NowDif = 1
		
		self.wm_title("2048")

		self.geometry('%dx%d' % ((self.SizeX+0.13)*100, (self.SizeY+1)*100))
		
		self.bind('<Key-Left>', self.MoveLeft)
		self.bind('<Key-Right>', self.MoveRight)
		self.bind('<Key-Up>', self.MoveUp)
		self.bind('<Key-Down>', self.MoveDown)
		
		self.Difct = IntVar()
		self.Difct.set(1)
		R1 = Radiobutton(self, text="Easy", variable=self.Difct, value=1)
		R2 = Radiobutton(self, text="Normal", variable=self.Difct, value=2)
		R3 = Radiobutton(self, text="Hard", variable=self.Difct, value=3)
		R1.grid(row=SizeY, column=0)
		R2.grid(row=SizeY, column=1)
		R3.grid(row=SizeY, column=2) 
		
		self.P1 = Label(self, text=self.Point, bg="blue", fg ="red", font = 50, width = 16,height = 2)
		self.P1.grid(row=SizeY+1,column=0, columnspan=2)

		B1 = Button(self, text="Restart", bg="green", fg="red",font = 30,width = 8,height = 2,command=self.Start)
		B1.grid(row=SizeY+1,column=2)
		B2 = Button(self, text="Exit", bg="yellow", fg="red",font = 30,width = 8,height = 2,command=exit)
		B2.grid(row=SizeY+1,column=3)

		self.Start()

	def Start(self):
		self.IsGameOver = False
		self.NowDif = self.Difct.get()
		self.Point = 0
		self.mat = [[0 for y in range(self.SizeY)] for x in range(self.SizeX)]
		self.gif = [[PhotoImage(file='./icon/block_%d.gif' % self.mat[x][y]) for x in range(self.SizeX)] for y in range(self.SizeY)]
		self.RandomCreate()
		self.Print()

	def MoveUp(self,e):
		if self.IsGameOver:
			return

		#print "Up"
		for x in range(self.SizeX):
			for y in range(self.SizeY):
				tx = x
				ty = y
				while self.Move(tx,ty,-1,0):
					tx += -1

		[rest, maxval] = self.Count()
		if rest == 0:
			self.Gameover()
			return 
		#
		if maxval == 2048:
			self.Gameover()
			return 
		#
		
		self.RandomCreate()
		self.Print()

	def MoveDown(self,e):
		if self.IsGameOver:
			return

		#print "Down"
		for x in range(self.SizeX-1,-1,-1):
			for y in range(self.SizeY):
				tx = x
				ty = y
				while self.Move(tx,ty,+1,0):
					tx += +1
		
		[rest, maxval] = self.Count()
		if rest == 0:
			self.Gameover()
			return 
		#
		if maxval == 2048:
			self.Gameover()
			return 
		#
		
		self.RandomCreate()
		self.Print()

	def MoveLeft(self,e):
		if self.IsGameOver:
			return
		
		#print "Left"
		for x in range(self.SizeX):
			for y in range(self.SizeY):
				tx = x
				ty = y
				while self.Move(tx,ty,0,-1):
					ty += -1
		
		[rest, maxval] = self.Count()
		if rest == 0:
			self.Gameover()
			return 
		#
		if maxval == 2048:
			self.Gameover()
			return 
		#
		
		self.RandomCreate()
		self.Print()

	def MoveRight(self,e):
		if self.IsGameOver:
			return
		
		#print "Right"
		for x in range(self.SizeX):
			for y in range(self.SizeY-1,-1,-1):
				tx = x
				ty = y
				while self.Move(tx,ty,0,+1):
					ty += +1
		
		[rest, maxval] = self.Count()
		if rest == 0:
			self.Gameover()
			return 
		#
		if maxval == 2048:
			self.Gameover()
			return 
		#
		
		self.RandomCreate()
		self.Print()

	def RandomCreate(self):
		for i in range(self.NowDif):
			[rest, maxval] = self.Count()
			if (rest == 0):
				self.Gameover()
				return 
			t = random.randint(0,rest-1)
			for x in range(self.SizeX):
				for y in range(self.SizeY):
					if (self.mat[x][y] == 0):
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

	def Gameover(self):
		DIF = ["","easy","normal","hard"]
		Message = SimpleDialog(self, text="You get %d Points in %s mode, good job!" % (self.Point, DIF[self.NowDif]), buttons= ["Yes"])
		
		self.IsGameOver = True

		return 
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
		#for x in range(self.SizeX):
		#	print self.mat[x]
		self.P1.config(text=str(self.Point))
	def Move(self,x,y,dx,dy):
		if self.mat[x][y] == 0:
			return 0
		if x+dx < 0 or x+dx >= self.SizeX:
			return 0
		if y+dy < 0 or y+dy >= self.SizeY:
			return 0

		MergeFlag = 1
		if self.mat[x+dx][y+dy] == self.mat[x][y]:
			MergeFlag = 0
			self.Point += self.mat[x][y]
		elif self.mat[x+dx][y+dy] == 0:
			MergeFlag = 1
		else:
			return 0
		
		self.mat[x+dx][y+dy] += self.mat[x][y]
		self.mat[x][y] = 0
		
		return MergeFlag