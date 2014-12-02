import Block

def Init():
        global mat
        global SizeX
        global SizeY
	mat = [[Block(0,x,y) for y in range(SizeY)] for x in range(SizeX)]
	RandomCreate(mat)
