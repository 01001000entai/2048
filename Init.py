import Block

def Init():
	global SizeY
	global SizeX
	mat = [[Block(0,x,y) for y in range(SizeY)] for x in range(SizeX)]
	RandomCreate(mat)
	return mat