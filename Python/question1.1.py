"Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data stuctures?"


"Since this is the first exercise, I will use this mostly to see how I can program test cases and get a deeper understanding of object oriented programming in Python"

"------------------------------------------"
def uniqueCharacters(mystring):
	for i in range(len(mystring)-1):
		for j in range(i+1,len(mystring)):
			if mystring[i]==mystring[j]:
				return False;
	return True;
	


def uniqueCharacters2(mystring):
	return len(set(mystring))==len(mystring)



"----------------------------------------------"


TestCases=['abce', '__', 'hola', '183fj;a', '', 'whatever', 'abcdefghjiklmnopqrust']

for case in TestCases:
	print 'Case: '+case+ ' is  '+str(uniqueCharacters2(case))

	
