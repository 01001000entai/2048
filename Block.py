#thr class of block

SizeX = 4
SizeY = 4
mat = [[Block(0,x,y) for y in range(SizeY)] for x in range(SizeX)]


class Block():
	def _init_(self,val=2,posx=0,posy=0):
		self.val = 2
		self.posx = 0
		self.posy = 0
	def Move(self,mat,dx,dy):
		MergeFlag = 0
		if self.posx+dx < 0 or self.posx+dx >= SizeX:
			return 0
		if self.posy+dy < 0 or self.posy+dy >= SizeY:
			return 0
		if mat[self.posx+dx][self.posx+dy].val == self.val:
			self.val *= 2
			MergeFlag = 1
		else:
			return 0
		mat[self.posx+dx][self.posx+dy] = self
		mat[self.posx+dx][self.posx+dy] = Block(0,self.posx,self.posy)
		self.posx += dx
		self.posy += dy
		return 1 + MergeFlag

