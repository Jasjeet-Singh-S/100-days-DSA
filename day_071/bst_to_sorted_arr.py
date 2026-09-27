'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def flattenBST(self, root):
        order = []
        self.inorder(root, order)

        if len(order) == 0:
            return None

        root2 = Node(order[0])
        ptr = root2

        for i in range(1, len(order)):
            ptr.right = Node(order[i])
            ptr = ptr.right

        return root2

    def inorder(self, root, arr):
        if root is None:
            return

        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)