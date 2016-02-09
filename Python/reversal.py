'''
1. Given a string, write a function or method that takes in that string, and returns the same string in reverse order.
Example: Given the string 'Hello', your program would return 'olleH'

'''

def stringReversal(s):
	
	newString=""
	for i in range(len(s)):
		newString+=s[len(s)-i-1]  #Just aggregate them backwards
	return newString



testCases=["Hello", "This is a string", "Reverse String","","s7r1ng w1th l3773r$ and ch4r4cters"]
for case in testCases:
	print case," --->",stringReversal(case)



