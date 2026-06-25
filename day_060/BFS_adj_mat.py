# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

from collections import deque

class Solution:
    def bfs(self, adj):
        visited = [False] * len(adj)
        result = []
        queue = deque([0])
        visited[0] = True
        while queue:
            curr_node = queue.popleft()
            # visited[curr_node] = True
            result.append(curr_node)
            for neighbour in adj[curr_node]:
                if visited[neighbour]==False:
                    queue.append(neighbour)
                    visited[neighbour]=True
        
        return result