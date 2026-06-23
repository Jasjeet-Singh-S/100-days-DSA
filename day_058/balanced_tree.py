# https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1

class Solution:
    def isBalanced(self, root):
        return self.dfsHeight(root)!=-1

    def dfsHeight(self, root):  # height of BT function modified to return -1 for our condition
        if root==None:
            return 0
        
        left_height = self.dfsHeight(root.left)
        right_height = self.dfsHeight(root.right)

        if left_height == -1 or right_height == -1:
            return -1
        
        if abs(left_height-right_height)>1:
            return -1
        else:
            return max(left_height, right_height) + 1  # +1 becasue of height of current level