from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        result = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            if node.left:
                queue.append((node.left, hd-1))
            if node.right:
                queue.append((node.right, hd+1))

            if hd not in result:
                result[hd] = node.data
            
        return [result[key] for key in sorted(result)]