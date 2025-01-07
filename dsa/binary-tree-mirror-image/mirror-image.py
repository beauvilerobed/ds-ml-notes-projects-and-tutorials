# Given a binary tree, write a function to determine whether the tree is a mirror
# image of itself. Two trees are a mirror image of each other if their root values
# are the same and the left subtree is a mirror image of the right subtree.

# example: [1,2,2,3,4,'None',3] --> False [1,2,2,3,4,4,3] --> True [1,2,2,3, None, None, None] --> False

# Solution runtime O(N) space complexity O(logN)

from binarytreegenerator import print_tree, make_tree

def check_sym(node):
    if not node: 
        return True
    
    return helper(node.left, node.right)

def helper(leftnode, rightnode):
    if leftnode is None and rightnode is None:
        return True
    if leftnode is None or rightnode is None:
        return False
    else:
        return leftnode.value == rightnode.value and \
            helper(leftnode.left, rightnode.right) and \
                helper(leftnode.right, rightnode.left)
    


def main():
    elems = input().split()
    elems = [elem if elem != 'None' else None for elem in elems]
    tree = make_tree(elems)
    print_tree(tree)

    if check_sym(tree):
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()