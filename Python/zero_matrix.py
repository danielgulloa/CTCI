'''
Write an algorithm such that if an element in an MxN matrix is 0, the entire row and column are set to 0
'''


def zero_matrix(mat):
	zeroPositions=[]
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if mat[i][j]==0:
				zeroPositions.append((i,j))
	mat2=mat
	for pos in zeroPositions:
		for j in range(len(mat[pos[0]])):
			mat2[pos[0]][j]=0
		for i in range(len(mat)):
			mat2[i][pos[1]]=0
	return mat2


def printMat(mat):
        for i in range(len(mat)):
                print mat[i]




testCases=[[[1,2,0],[4,5,6],[7,8,9]], [[1,2,0,4],[5,6,7,8],[9,10,0,12]]]

for case in testCases:
	printMat(case)
	print "Becomes:"
	printMat(zero_matrix(case))
	print "\n"


	
