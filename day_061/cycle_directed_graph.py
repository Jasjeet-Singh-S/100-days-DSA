class Solution:
    def DFS(self, node, visited, path_visited, adj):
        visited[node] = 1
        path_visited[node] = 1
        for adjacent_node in adj[node]:
            if visited[adjacent_node]==0:
                if self.DFS(adjacent_node, visited, path_visited, adj)==True:
                    return True
            elif path_visited[adjacent_node]==1:
                return True
        path_visited[node] = 0
        return False

    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v = edge
            adj[u].append(v)

        visited = [0] * V
        path_visited = [0] * V
        for i in range(V):
            if visited[i]==0:
                if self.DFS(i, visited, path_visited, adj)==True:
                    return True
        return False