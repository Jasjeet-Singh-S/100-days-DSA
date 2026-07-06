# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this is what i wrote but it fails a case like this 
    #     5
    #    / \
    #   4   6
    #      / \
    #     3   7
# because it only check local, so we need a approach that maintains boundary of high and low 

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         curr = True
#         if root.left is not None:
#             left = self.isValidBST(root.left)
#             curr = curr and root.val>root.left.val
#         else:
#             left = True  # cant have left be null otherwise final and operation will also return null
#         if root.right is not None:
#             right = self.isValidBST(root.left)
#             curr = curr and root.val<root.right.val
#         else:
#             right = True  # same here

#         return left and right and curr

from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=-inf, high=inf) -> bool:
        if root is None:
            return True
        if not (low < root.val < high):
            return False
        
        left = self.isValidBST(root.left, low, root.val)  # tighten the upper bound
        right = self.isValidBST(root.right, root.val, high)  # tighten the lower bound

        return left and right