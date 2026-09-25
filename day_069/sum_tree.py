''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        if root==None:
            return 0
        left_sum = self.toSumTree(root.left)
        right_sum = self.toSumTree(root.right)
        temp = root.data
        root.data = left_sum+right_sum
        return root.data+temp