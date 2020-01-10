class Node:
	def __init__(self, value, lchild=None, rchild=None):
		self.value = value
		self.lchild = lchild
		self.rchild = rchild

root_node = Node(1)
n, q = map(int,input().split())

def find_parent_node(node, parent):
	# print("Current value",node.value)
	if node.value == parent:
		# print("Node",node)
		return node
	
	if node.lchild is not None:
		# print("Checking on left side")
		leftnode = find_parent_node(node.lchild, parent)
		if leftnode is not None:
			return leftnode
	
	# print("current node",node.value)
	if node.rchild is not None:
		# print("Checking on right side")
		rnode = find_parent_node(node.rchild, parent)
		if rnode is not None:
			return rnode


def add_node(current, value, pos):
	new_node = Node(value)
	if pos=='R':
		current.rchild = new_node
		# print("Node added successfull on right side")
	if pos=='L':
		current.lchild = new_node
		# print("Node added successfull on left side")

def display(root):
	if root is not None:
		print(root.value, end=' ')
	
	if root.lchild is not None:
		display(root.lchild)
	
	if root.rchild is not None:
		display(root.rchild)

def findmirrorRec(root_node, mirror_of, lpointer, rpointer):
	if lpointer == None or rpointer == None:
		return -1
	
	# lpointer = root_node.lchild
	# rpointer = root_node.rchild
	
	if lpointer.value == mirror_of:
		return rpointer.value
	
	if rpointer.value == mirror_of:
		return lpointer.value
	
	# Recuring only external node
	extern = findmirrorRec(root_node, mirror_of, lpointer.lchild, rpointer.rchild)
	if extern != -1:
		return extern
	
	# on external found recurring internal node
	return findmirrorRec(root_node, mirror_of, lpointer.rchild, rpointer.lchild)

def findmirror(root_node, mirror_of):
	if root_node == None:
		return -1
		
	if root_node.value == mirror_of:
		return root_node.value
	
	return findmirrorRec(root_node, mirror_of, root_node.lchild, root_node.rchild)

for i in range(n-1):
	parent, value, pos = map(str, input().split())
	found_node = find_parent_node(root_node, int(parent))
	# print(found_node)
	add_node(found_node, int(value), pos)
# display(root_node)
for each in range(q):
	mirror_of = int(input())
	print(findmirror(root_node, mirror_of))
