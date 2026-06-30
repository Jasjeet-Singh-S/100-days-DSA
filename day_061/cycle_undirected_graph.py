class Solution:
    def DFS(self, node, parent, visited, adj):
        visited[node] = 1
        for adjacent_node in adj[node]:
            if visited[adjacent_node]==0:
                if self.DFS(adjacent_node, node, visited, adj)==True:
                    return True
            elif adjacent_node!=parent:
                return True
        return False

    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * V
        for i in range(V):
            if visited[i]==0:
                if self.DFS(i, -1, visited, adj)==True:
                    return True
        return False