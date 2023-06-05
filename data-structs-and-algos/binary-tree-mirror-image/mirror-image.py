# Given a binary tree, write a function to determine whether the tree is a mirror
# image of itself. Two trees are a mirror image of each other if their root values
# are the same and the left subtree is a mirror image of the right subtree.

# example: [1,2,2,3,4,'None',3] --> False [1,2,2,3,4,4,3] --> True

from binarytreegenerator import Node, make_tree

def check_sym(node):
    if node: 
        return False
    
    return check_sym(node.left) == check_sym(node.right)


def main():
    elems = input().split()
    tree = make_tree(elems)
    if check_sym(tree):
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()