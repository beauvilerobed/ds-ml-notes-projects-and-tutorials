# Given a binary tree, write a function to determine the diameter of the tree, which is
# the longest path between any two nodes

# solution: runtime O(N) space complexity O(N)

from binarytreegenerator import make_tree, print_tree

def return_diam(node):
    def helper(node, diameter):
        if node == None:
            return 0, diameter
        left, diameter = helper(node.left, diameter)
        right, diameter = helper(node.right, diameter)
        diameter = max(diameter, left+right)
        return max(left, right) + 1, diameter
    depth, diameter = helper(node, 0)
    return diameter

def main():
    input1 = [float(val) for val in input().split()]
    tree1 = make_tree(input1)
    print_tree(tree1)
    print(return_diam(tree1))


if __name__=="__main__":
    main()
