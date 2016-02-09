'''
1.6) String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your method should return the original string. You can assume the string has only upper case and lowercase letters (a-z)

'''

def stringCompression(mystring):

	compressed=mystring[0]
	thiscount=1
	for i in range(1,len(mystring)):
		if mystring[i]==mystring[i-1]:
			thiscount+=1
		else:
			compressed+=str(thiscount)+mystring[i]
			thiscount=1

	compressed+=str(thiscount)
	if len(compressed)<len(mystring):
		return compressed
	else:
		return mystring



testCases=["aabcccccaaa", "abcdefghijklm", "aaaaaaaaaaabbbcdeffffgh"]
for case in testCases:
	print case," becomes ", stringCompression(case)



