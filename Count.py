#Count the number of nonzero-block and the maxval

import Block

def Count(mat):
	NumofNonzero = 0
	MaxVal = 0
	for t in mat:
		if (t.val > 0) NumofNonzero++
		if (MaxVal < t.val) MaxVal = t.val
	return  [NumofNonzero, MaxVal]
