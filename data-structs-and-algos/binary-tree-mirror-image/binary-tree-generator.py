
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def insert(temp,data):
   que = []
   que.append(temp)
   while (len(que)):
      temp = que[0]
      que.pop(0)
      if (not temp.left):
         if data is not None:
            temp.left = Node(data)
         else:
            temp.left = Node(0)
         break
      else:
         que.append(temp.left)
      if (not temp.right):
         if data is not None:
            temp.right = Node(data)
         else:
            temp.right = Node(0)
         break
      else:
         que.append(temp.right)


def make_tree(elements):
   Tree = Node(elements[0])
   for element in elements[1:]:
      insert(Tree, element)
   return Tree

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(" " * 4 * level + "->", node.value)
        print_tree(node.left, level + 1)

tree1 = make_tree([1,2,2,3,4,4,3])
tree2 = make_tree([1,2,2,3,4,'None',3])

print_tree(tree1)
print_tree(tree2)
