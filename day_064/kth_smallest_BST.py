# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.result = None
        self.k = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        self.k = k
        self.inorder(root)
        return self.result

    def inorder(self, root):  # modified inorder traversal
        if root is None:
            return 
        
        self.inorder(root.left)  # go left

        self.count += 1  # process this noce

        if self.count == self.k:
            self.result = root.val
            return
        
        self.inorder(root.right)  # go right

        return self.result