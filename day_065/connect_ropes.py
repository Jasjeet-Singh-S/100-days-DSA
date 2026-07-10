# https://www.geeksforgeeks.org/dsa/connect-n-ropes-minimum-cost/
import heapq
class Solution:
   def minCost(self, arr):
    # code here
    heapq.heapify(arr)
    res = 0
    while arr:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        res += first + second
        heapq.heappush(arr, first+second)
    return res