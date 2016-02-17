'''
Given a sorted (increasing order) array with unique integer elements,write an algorithm to create a binary search tree with minimal height
'''

import treeNode as t


def minTree(inputArray,Tree=t.Node("root")):
	if len(inputArray)>0:
		midpoint=len(inputArray)/2
		midvalue=inputArray[midpoint]
		Tree.name="Node"
		Tree.value=midvalue
		Tree.left=t.Node()
		Tree.right=t.Node()
		minTree(inputArray[0:midpoint],Tree.left)
		minTree(inputArray[(midpoint+1):],Tree.right)
		return Tree
	return




testCases=[[2,3,4,6,8,10,12,16],[10,12,14,16,18,30],[]]


for case in testCases:
	T1=minTree(case)
	t.inOrderTraversal(T1)





