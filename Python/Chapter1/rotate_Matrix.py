'''
Rotate Matrix 90 degrees
'''



def rotate(mat1,n):
	mat=mat1
	for layer in range(n/2):
		first=layer
		last=n-1-layer
		for i in range(first,last):
			offset=i-first
			top=mat[first][i]
			mat[first][i]=mat[last-offset][first]
			mat[last-offset][first]=mat[last][last-offset]
			mat[last][last-offset]=mat[i][last]
			mat[i][last]=top
	return mat

def printMat(mat):
	for i in range(len(mat)):
		print mat[i]



testCases=[[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]]

for case in testCases:
	printMat(case)
	print "Becomes:"
	printMat(rotate(case,len(case)))
	print "\n"




