# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        pq = self.tree2arr(p)
        qq = self.tree2arr(q)
        pi = self.node2int(pq)
        qi = self.node2int(qq)
        return pi==qi

    def tree2arr(self, root): 
        if root == None:
            return [None]
        
        queue = []
        queue.append(root)
        i = 0

        while i<len(queue):
            curr_node = queue[i]
            if curr_node==None:
                i+=1
            else:
                i += 1
                if curr_node.left:
                    queue.append(curr_node.left)
                else:
                    queue.append(None)
                if curr_node.right:
                    queue.append(curr_node.right)
                else:
                    queue.append(None)
        
        return queue
    
    def node2int(self, arr):
        for i in range(len(arr)):
            node = arr[i]
            if node!=None:
                arr[i] = node.val
        return arr