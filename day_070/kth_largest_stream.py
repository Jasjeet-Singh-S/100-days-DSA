import heapq

class Solution:
    def kthLargest(self, arr, k):
        heap = []
        output = []
        minimum = 0
        for elem in arr:
            if minimum>elem:
                heapq.heappush(heap, minimum)
            else:
                heapq.heappush(heap, elem)
            if len(heap)==k:
                minimum = heapq.heappop(heap)
                output.append(minimum)
            else:
                output.append(-1)
        return output