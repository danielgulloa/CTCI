'''
Assume you have a method issubstring that tells you if a string is substring of another. Given two strings write a method to tell if s1 is substring of s2 using only one call to the issubstring method.
'''

def isSubstring(s1,s2):
	return (s1 in s2) or (s2 in s1)



def stringRotation(s1,s2):
	if len(s1)!=len(s2) or len(s1)==0:
		return False
	midpoint=len(s1)/2
	x=s1[:midpoint]
	y=s1[midpoint:]
	return isSubstring(y+x+y+x,s2)



testCases=[('waterbottle','erbottlewat'),('not rotation','ot rotation')]

for case in testCases:
	print case[0],case[1],"---->", stringRotation(case[0],case[1])
