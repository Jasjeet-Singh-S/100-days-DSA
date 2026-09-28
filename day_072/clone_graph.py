"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        return self.dfs(node, old_to_new) if node else None

    def dfs(self, node, old_to_new):
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(self.dfs(nei, old_to_new))

        return copy