# https://leetcode.com/problems/binary-tree-level-order-traversal/

# class Solution:
#     def levelOrder(self, root):
#         if not root:
#             return []

#         queue = [[root]]

#         val_queue = [[root.val]]

#         i = 0

#         while i<len(queue):
#             nodes = queue[i]
#             subqueue = []
#             val_subqueue = []
#             for node in nodes:
#                 if node.left:
#                     subqueue.append(node.left)
#                     val_subqueue.append(node.left.val)
#                 if node.right:
#                     subqueue.append(node.right)
#                     val_subqueue.append(node.right.val)
#             queue.append(subqueue)
#             val_queue.append(val_subqueue)
#             i += 1
        
#         return val_queue

# the above is what i wrote but its getting a memory limit exceeded error (MLE) because we maintain the list for the entirety of program

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level_values = []
            
            # Process exactly the nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level_values)
            
        return result