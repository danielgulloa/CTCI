'''
1.5) One Away: There are 3 types of edits that can be performed on strings: insert a character, remove a character or replace a character. Given two strings, write a function to check if they are one dit (or zero edits) away. Example: pale, ple -> true    pales, pale  --> true    pale, bake --> False
'''



def countInsertRemoves(str1,str2):
	return abs(len(str1)-len(str2))


def countReplace(str1,str2):
	if (len(str1)!=len(str2)):
		return 0
	else:
		lst1=list(str1)
		lst2=list(str2)
		replaces=0
		for i in range(len(lst1)):
			if lst1[i]!=lst2[i]:
				replaces+=1
		return replaces	
	


def oneAway(str1,str2):
	if str1==str2:
		return True
	if abs(len(str1)-len(str2))>1:
		return False
	

	changes=0
	changes+=countInsertRemoves(str1,str2)
	changes+=countReplace(str1,str2)

	return (changes<2)



testCases=[("pale", "ple"),("pales", "pale"), ("pale","bale"), ("pale","bake")]
for case in testCases:
	print case[0], ",",case[1], "---->", oneAway(case[0], case[1])



	



	
