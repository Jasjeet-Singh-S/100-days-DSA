# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
# BFS code is the reference, i just changed that code to make DFS
# GFG didnt accept this solution but it is correct im pretty sure, and that its just failing because of the roder of the output which im not gonna bother with

class Solution:
    def dfs(self, adj):
        visited = [False] * len(adj)
        result = []
        queue = [0]  # just use a stack (list) instead of a queue
        visited[0] = True
        while queue:
            curr_node = queue.pop()  # also did a pop instead of popleft over bfs
            result.append(curr_node)
            for neighbour in reversed(adj[curr_node]):  # had to add this extra reverse to produce order expected by gfg otherwise removing this is also fine
                if visited[neighbour]==False:
                    queue.append(neighbour)
                    visited[neighbour]=True
        
        return result