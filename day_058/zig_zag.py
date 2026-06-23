# https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1

from collections import deque

class Solution:
    def zigZagTraversal(self, root):
        array = self.levelOrder(root)
        result = []
        for i in range(len(array)):
            if i%2==0:
                for number in array[i]:
                    result.append(number)
            else:
                end = len(result)
                for number in array[i]:
                    result.insert(end, number)
        return result

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
                current_level_values.append(node.data)
                
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level_values)
            
        return result