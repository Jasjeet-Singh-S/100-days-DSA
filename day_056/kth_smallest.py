import heapq

class Solution:
    def kthSmallest(self, arr, k):
        pq = []
        for i in range(len(arr)):
            heapq.heappush(pq, -arr[i])  # push elements into max heap, note its a min heap made max heap using the minus sign
            if len(pq)>k:
                heapq.heappop(pq)
        
        return -pq[0]

if __name__=="__main__":
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k = 4
    expected_output = 5
    actual_output = Solution().kthSmallest(arr, k)
    if actual_output==expected_output:
        print("pass")
    else:
        print("fail")
        print(actual_output)