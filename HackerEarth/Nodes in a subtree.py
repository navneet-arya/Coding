class Node:
	def __init__(self, key, index, count=1, lchild=None, rchild=None):
		self.key = key
		self.index = index
		self.subtree = count
		self.lchild = lchild
		self.rchild = rchild


def find_parent_node(node, parent):
	if node.index == parent:
		return node
	
	if root_node.lchild is not None:
		left = find_parent_node(node.lchild, parent)
		if left is not None:
			return left
	
	if root_node.rchild is not None:
		right = find_parent_node(node.rchild, parent)
		if right is not None:
			return right

def add_node(node, key, index):
	new_node = Node(key, index)
	# print("In add node",key,index)
	if node.lchild is None:
		node.lchild = new_node
		# print("Added on lchild", key, index)
	
	elif node.rchild is None:
		node.rchild = new_node
		# print("Added on rchild", key, index)

def display(root):
	if root is not None:
		print(root.key, root.index,root.subtree, end='-')
	
	if root.lchild is not None:
		display(root.lchild)
	
	if root.rchild is not None:
		display(root.rchild)

def SubTreeCount(node):
	if node is not None:
		# print(node.key)
		if node.lchild is None and node.rchild is None:
			# print("In none:",node.key)
			# node.subtree = 1
			return node.subtree
			
		if node.lchild is not None or node.rchild is not None:
			# print("---node",node.key, node.subtree)
			node.subtree = node.subtree + SubTreeCount(node.lchild)\
							+ SubTreeCount(node.rchild)

def subtree(node, index, node_value):
	if node.index == index and node.key == node_value:
		return node.subtree-1
	
	if node.lchild is not None:
		ltree = subtree(node.lchild, index, node_value)
		if ltree is not None:
			return ltree
	
	if node.rchild is not None:
		rtree = subtree(node.rchild, index, node_value)
		if rtree is not None:
			return rtree

n, q = map(int, input().split())
string = input()

root_node = Node(string[0],1)
for i in range(1,n):
	parent, nextindex = map(int, input().split())
	found_node = find_parent_node(root_node, parent)
	# print(string[i], nextindex)
	add_node(found_node, string[i], nextindex)

SubTreeCount(root_node)
# display(root_node)

for i in range(q):
	index, node_value = map(str,input().split())
	print(subtree(root_node, int(index), node_value))
