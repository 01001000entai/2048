def Init():
	mat = [[Block(0,x,y) for y in range(SizeY)] for x in range(SizeX)]
	RandomCreate(mat)
