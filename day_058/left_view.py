# https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1

# the first node of every level is the left view (and last node is rifght view)

from collections import deque

class Solution:
    def leftView(self, root):
        level_order = self.levelOrder(root)
        left_view = []
        for i in range(len(level_order)):
            left_view.append(level_order[i][0])
        return left_view

    def levelOrder(self, root):  # from level order traversal question as it is
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
                current_level_values.append(node.data)
                
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level_values)
            
        return result