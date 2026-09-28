''' Binary Tree Node Structure
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def getCount(self, root: 'Node', l: int, h: int) -> int:
        if root is None:
            return 0

        count = 0

        if l <= root.data <= h:
            count = 1

        if root.data > l:
            count += self.getCount(root.left, l, h)

        if root.data < h:
            count += self.getCount(root.right, l, h)

        return count