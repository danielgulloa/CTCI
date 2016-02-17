class Node:
	def __init__(self,name="",value=None,left=None,right=None):
		self.name=name
		self.value=value
		self.left=left
		self.right=right
		self.marked=False
		self.parent=None

	def sibling(self):
		if self.parent.left==self:
			return self.parent.right
		return self.parent.left


def inOrderTraversal(N):
	if N!=None:
		visit(N)
		inOrderTraversal(N.left)
		inOrderTraversal(N.right)



def visit(N):
	print N.name,N.value





def bfs(root):
	import Queue as q
	queue=q.Queue()
	root.maked=True
	queue.put(root)

	while(not queue.empty()):
		n=queue.get()
		visit(n)
		
				
