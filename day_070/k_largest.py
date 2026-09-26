import heapq

class Solution:
	def kLargest(self, arr, k):
		# code here
		n = len(arr)
		heap = []
        output = []
        for elem in arr:
            heapq.heappush(heap, -elem)
            if len(heap)==n-k+1:
                minimum = heapq.heappop(heap)
                output.append(-minimum)

        output.sort(reverse=True)
        
        output.sort(reverse=True)