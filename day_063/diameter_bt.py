# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def diameter(self, root):
        self.diameter = 0
        self.height(root, self.diameter)
        return self.diameter

    def height(self, node, diameter):
        if node==None:
            return 0
        
        lh = self.height(node.left, self.diameter)
        rh = self.height(node.right, self.diameter)

        self.diameter = max(self.diameter, lh+rh)

        return 1+max(lh,rh)