import math
import heapq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))

        dists = [math.inf] * V
        dists[src] = 0

        pq = []
        heapq.heappush(pq, [0,src])

        while pq:
            dist, node = heapq.heappop(pq)
            
            if dist > dists[node]:  # stale entry, skip it
                continue

            for adjacent in adj[node]:
                edge_weight = adjacent[1]
                adj_node = adjacent[0]

                if dist+edge_weight<dists[adj_node]:
                    dists[adj_node]=dist+edge_weight
                    heapq.heappush(pq, [dists[adj_node], adj_node])

        return dists