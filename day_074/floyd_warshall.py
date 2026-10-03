# https://www.youtube.com/watch?v=YbY8cVwWAvw&t=1480s
# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

class Solution:
    def floydWarshall(self, dist):
        n = len(dist)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != 100000000 and dist[k][j] != 100000000:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][k] + dist[k][j]
                        )