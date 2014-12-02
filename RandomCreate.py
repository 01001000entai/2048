#Create a block in random

import random
import Count

def RandomCreate(mat):
	[rest, maxval] = Count(mat)
	t = random.randint(0,rest-1)
	for x in range(SizeX):
		for y in range(SizeY):
			if t < 0:	break
			elif t > 0: 	t--
			else:		mat[x][y] = Block(random.randint(0,1)*2+2,x,y)

				
