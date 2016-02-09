'''
Given two strings, write a method to decide if one is a permutation of the other
'''


#--------------------------------------------------------------
def isPermutation(str1, str2):
	return set(str1)==set(str2) and len(str1)==len(str2)

#--------------------------------------------------------------



testCases=[('abcd', 'bcda'), ('a13', 'a14'), ('aaaaaa', 'aaaa')]
for case in testCases:
	print 'Are '+case[0]+' and '+case[1]+' a permutation? '+ str(isPermutation(case[0], case[1]))
