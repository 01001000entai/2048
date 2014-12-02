#Move

import Block
import RandomCreate
import Print
import Count

def MoveUp():
	for x in range(SizeX):
		for y in range(SizeY):
			while mat[x][y].Move(mat,-1,0):

	[rest,maxval] = Count(mat)
	if rest == 0:
		exit()
`		#
	if maxval == 2048:
		exit()
		#
	
	RandomCreate(mat)
	Print(mat)


def MoveDown():
	for x in range(SizeX-1,-1,-1):
		for y in range(SizeY):
			while mat[x][y].Move(mat,+1,0):

	[rest,maxval] = Count(mat)
	if rest == 0:
		exit()
`		#
	if maxval == 2048:
		exit()
		#
	
	RandomCreate(mat)
	Print(mat)



def MoveLeft():
	for x in range(SizeX):
		for y in range(SizeY):
			while mat[x][y].Move(mat,0,-1):

	[rest,maxval] = Count(mat)
	if rest == 0:
		exit()
`		#
	if maxval == 2048:
		exit()
		#
	
	RandomCreate(mat)
	Print(mat)

def MoveRight():
	for x in range(SizeX):
		for y in range(SizeY-1,-1,-1):
			while mat[x][y].Move(mat,0,1):

	[rest,maxval] = Count(mat)
	if rest == 0:
		exit()
`		#
	if maxval == 2048:
		exit()
		#
	
	RandomCreate(mat)
	Print(mat)

