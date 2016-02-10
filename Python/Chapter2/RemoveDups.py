'''
Write code to remove duplicates from an unsorted linked list
Try not using another data structure
'''

import myNode as N



def removeDups(linkedList):
	current=linkedList
	while(current!=None):
		runner=current
		while(runner.next!=None):
			if runner.next.data==current.data:
				runner.next=runner.next.next
			else:
				runner=runner.next

		current=current.next	




#Test Cases
#Regular case
llist1=N.Node(5)
llist1.appendToTail(6)
llist1.appendToTail(7)
llist1.appendToTail(7)
llist1.appendToTail(8)
llist1.appendToTail(9)

#Three of a kind
llist2=N.Node(5)
llist2.appendToTail(6)
llist2.appendToTail(7)
llist2.appendToTail(7)
llist2.appendToTail(7)
llist2.appendToTail(9)


#Two duplicates
llist3=N.Node(5)
llist3.appendToTail(6)
llist3.appendToTail(7)
llist3.appendToTail(7)
llist3.appendToTail(8)
llist3.appendToTail(9)
llist3.appendToTail(9)
llist3.appendToTail(10)

#Empty list
llist4=N.Node()

testCases=[llist1,llist2,llist3,llist4]
for case in testCases:
	case.toString()
	print "Becomes"
	removeDups(case)
	case.toString()
	print "------------------"








	


