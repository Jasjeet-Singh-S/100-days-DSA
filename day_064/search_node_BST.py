# https://www.geeksforgeeks.org/problems/search-a-node-in-bst/1

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def search(self, root, key):
        # code here
        node = root
        while node is not None:
            if key==node.data:
                return True
            elif key>node.data:
                node = node.right
            else:
                node = node.left
        return False