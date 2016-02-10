'''
Implement a function which reverses a string
(The original question is Implement a function void reverse(char+ str) in C or C++ which reverses a null-terminated string)
'''

def reverse(mystring):
	newstr="";
	n=len(mystring)
	for i in range(n):
		newstr+=mystring[n-i-1]
	return newstr;


testCases=['anagram', 'hello', '', 'whatever', 'another test case']

for case in testCases:
	print "String: "+case+" is reversed and the result is "+reverse(case)


