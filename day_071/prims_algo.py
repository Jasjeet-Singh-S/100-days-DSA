import heapq

# clarification: this is slight modification of prims algo here not exactly prims algo, because we're only returning the weight of MST not the MST itself, so we wont carry the parent node in the priority queue

class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        heap = []  # min heap or priority queue
        visited = [0] * V
        sum = 0

        # create adjacency list
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, w = edge
            adj[u].append([v, w])
            adj[v].append([u, w])

        # weight, node
        heapq.heappush(heap, [0,0])
        while heap:
            weight, node = heapq.heappop(heap)

            if visited[node]==1:
                continue
            else:
                # add to visited
                visited[node] = 1
                sum += weight
                # in case someone asked for mst we wouldve taken the parent and stored it in a list at this step
                for AdjNode, wt in adj[node]:
                    if visited[AdjNode]==0:
                        heapq.heappush(heap, [wt, AdjNode])

        return sum