# https://www.geeksforgeeks.org/problems/normal-bst-to-balanced-bst/1

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def balanceBST(self,root):
        if not root:
            return None
        sorted_order = []
        self.inorder(root,sorted_order)
        return self.newBST(sorted_order)

    def newBST(self, sorted_order):
        if len(sorted_order)==0:
            return None
        n = len(sorted_order)
        new_root = sorted_order[n//2]
        new_root.left = self.newBST(sorted_order[:n//2])
        new_root.right = self.newBST(sorted_order[(n//2)+1:])

        return new_root

    def inorder(self, root, order):
        if root.left:
            self.inorder(root.left, order)
        order.append(root)
        if root.right:
            self.inorder(root.right, order)