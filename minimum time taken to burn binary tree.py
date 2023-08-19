class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def newNode(val):
	return Node(val)

node = None

def findParent(root, p, parent, start):
	if not root:
		return
	parent[root.val] = p
	if root.val == start:
		global node
		node = root
	findParent(root.left, root, parent, start)
	findParent(root.right, root, parent, start)

def amountOfTime(root, start):
	parent = [None] * 100005
	findParent(root, None, parent, start)

	visited = [False] * 100005

	q = []
	q.append(node)
	visited[start] = True

	result = -1

	while len(q) > 0:
		n = len(q)
		for i in range(n):
			curr = q.pop(0)
			currNode = curr.val

			if parent[currNode] and not visited[parent[currNode].val]:
				visited[parent[currNode].val] = True
				q.append(parent[currNode])

			if curr.left and not visited[curr.left.val]:
				visited[curr.left.val] = True
				q.append(curr.left)

			if curr.right and not visited[curr.right.val]:
				visited[curr.right.val] = True
				q.append(curr.right)

		result += 1

	return result

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.left.right = newNode(7)
root.right.right = newNode(6)
root.right.left = newNode(5)

start = 2

result = amountOfTime(root, start)
print(result)
