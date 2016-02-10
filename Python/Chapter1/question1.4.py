def replaceSpace(mystring):
	return mystring.replace(' ','%20')




#This was too easy, I guess they wanted to push the characters within the string:

#-------------------------------------------------------------
def push2ToRight(mylist,position):
	n=len(mylist)
	for i in range(n-position-1):
		mylist[n-i-1]=mylist[n-i-3]
		mylist[n-i-2]=mylist[n-i-4]
	return mylist



def replaceSpace2(mystring):
	mylist=list(mystring)
	for i in range(len(mystring)):
		if mylist[i]==' ':
			push2ToRight(mylist,i)
			mylist[i]='%'
			mylist[i+1]='2'
			mylist[i+2]='0'
	return ''.join(mylist)

#-------------------------------------------------------------


testCases=['case 1  ','Mr John Smith    ']


for case in testCases:
	print case+' Replaced with symbol becomes: '+replaceSpace2(case)


