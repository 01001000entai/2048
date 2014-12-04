#thr class of block

global SizeX
global SizeY

SizeX = 4
SizeY = 4

class Block(object):
	val = 0
	posx = 0
	posy = 0
	def __init__ (self,val,posx,posy):
		self.val = val
		self.posx = posx
		self.posy = posy
	def Move (self,mat,dx,dy):
		MergeFlag = 0
		if self.posx+dx < 0 or self.posx+dx >= SizeX:
			return 0
		if self.posy+dy < 0 or self.posy+dy >= SizeY:
			return 0
		if mat[self.posx+dx][self.posy+dy].val == self.val:
			self.val *= 2
			MergeFlag = 1
		else:
			return 0
		mat[self.posx+dx][self.posx+dy] = self
		mat[self.posx+dx][self.posx+dy] = Block(0,self.posx,self.posy)
		self.posx += dx
		self.posy += dy
		return 1 + MergeFlag

