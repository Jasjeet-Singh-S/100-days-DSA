# https://leetcode.com/problems/invert-binary-tree/

from collections import deque

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        queue = deque([root])

        while queue:
            current = queue.popleft()

            # Swap the children
            current.left, current.right = current.right, current.left

            # Add children to the queue to continue traversal
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return root
    
# felt pretty similar to max depth