# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            if p.val < curr.val and q.val < curr.val:
                # Both are in the left subtree
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                # Both are in the right subtree
                curr = curr.right
            else:
                # We found the split point (the LCA)
                return curr