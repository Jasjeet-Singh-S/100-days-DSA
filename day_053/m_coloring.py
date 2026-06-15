# User function Template for python3

class Solution:
    def is_safe(self, v, adj, col, c):
        # Check if color c can be assigned to vertex v
        for neighbor in adj[v]:
            if col[neighbor] == c:
                return False
        return True

    def solve(self, v, adj, col, m, n):
        if v == n:
            return True  # all vertices colored successfully

        for c in range(1, m + 1):
            if self.is_safe(v, adj, col, c):
                col[v] = c
                if self.solve(v + 1, adj, col, m, n):
                    return True
                col[v] = 0  # backtrack

        return False

    def graphColoring(self, n, edges, m):
        adj = [[] for _ in range(n)]
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)

        col = [0] * n
        return self.solve(0, adj, col, m, n)
                

if __name__ == "__main__":
    v = 4
    m = 3
    edges = [[0, 1], [1, 3], [2, 3], [3, 0], [0, 2]]
    if Solution().graphColoring(v, edges, m):
        print("pass")
    else:
        print("fail")