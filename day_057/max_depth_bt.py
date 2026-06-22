# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# i came up with this below solution but this will fail in an unbalanced tree

# import math

# class Solution:
#     def maxDepth(self, root):
#         if root == None:
#             return 0
        
#         queue = []
#         queue.append(root)
#         i = 0
#         while i<len(queue):
#             curr_node = queue[i]
#             if curr_node==None:
#                 i+=1
#             else:
#                 i += 1
#                 queue.append(curr_node.left)
#                 queue.append(curr_node.right)

#         return (math.ceil(math.log2(len(queue)))-1)

from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.next:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level

if __name__=="__main__":
    root = [3,9,20,None,None,15,7]