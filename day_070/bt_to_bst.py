'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def binaryTreeToBST(self, root):
        arr = []

        self.Tree2arr(root, arr)
        arr.sort()

        self.i = 0
        self.inorder(root, arr)

    def Tree2arr(self, root, arr):
        if root is None:
            return

        self.Tree2arr(root.left, arr)
        arr.append(root.data)
        self.Tree2arr(root.right, arr)

    def inorder(self, root, arr):
        if root is None:
            return

        self.inorder(root.left, arr)

        root.data = arr[self.i]
        self.i += 1

        self.inorder(root.right, arr)