class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v = edge
            adj[u].append(v)
        
        vis = [0] * V
        stack = []

        for i in range(V):
            if vis[i]!=1:
                self.DFS(i, vis, stack, adj)

        ans = []
        while stack:
            ans.append(stack.pop())
        
        return ans
    
    def DFS(self, node, vis, stack, adj):
        vis[node] = 1
        for adjacent in adj[node]:
            if vis[adjacent]!=1:
                self.DFS(adjacent, vis, stack, adj)
        stack.append(node)