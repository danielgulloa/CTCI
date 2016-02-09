'''
 Palindrome Permutation: Given a string, write a function to check if it is a permutation
of a palindrome. Example: Tact Coa  -> True   (e.g. taco cat, atco cta, etc)
'''


def palindromePermutation(mystring):

	mylist=list(mystring.replace(" ","").lower())
	mydict={}
	for letter in mylist:
		if letter in mydict.keys():
			mydict[letter]+=1
		else:
			mydict[letter]=1

	odds=0
	for key in mydict.keys():
		if mydict[key]%2==1:
			odds+=1 
	


	return (odds<2)




testCases=["tact coa","taco cat", "probably not", "anagram", "a man a plan Panama a canal","daba arroz a la zorra el abad", "anita la tina lava","", " "]

for case in testCases:
	print case, " ---> ",palindromePermutation(case)
	

