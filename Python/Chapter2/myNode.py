class Node:
	def __init__(self, data=None):
		self.next=None
		self.data=data
	def appendToTail(self,data):
		end=Node(data)
		while(self.next!=None):
			self=self.next
		self.next=end
	def toString(self):
		head=self
		print head.data
		while(head.next!=None):
			head=head.next
			print head.data
	def delete(self,data):
		head=self
		if head.data==data:
			return head.next
		while head.next!=None:
			if head.next.data==data:
				head.next=head.next.next
				return head
			head=head.next
		return head


			
def deleteNode(head,d):
	n=head
	if n.data==d:
		return head.next
	while n.next!=None:
		if n.next.data==d:
			n.next=n.next.next;
			return head #head didnt change
		n=n.next
	return head
