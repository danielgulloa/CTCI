'''
Given a string, return the character count for each distinct character in the string.
 Example: "abacca" -> a: 3, b: 1, c: 2
'''


def countChars(s):
	h={}  #a Hash table to keep count
	for i in range(len(s)):
		if s[i] in h.keys():   #If we have seen it before, just add one
			h[s[i]]+=1
		else:
			h[s[i]]=1   #Otherwise, this is the first time we see this character
	return h



testCases=["abacca", "badadaadddaaddca", "", "a--()%%ppqewr"]
for case in testCases:
	print case," ---> ", countChars(case)
