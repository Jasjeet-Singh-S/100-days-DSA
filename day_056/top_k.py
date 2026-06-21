from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        return heapq.nlargest(k, counts.keys(), key=counts.get)
    # O(N) map creation + O(NLogK) for returning top K


if __name__=="__main__":
    arr = [1,1,1,2,2,3]
    k = 2
    expected_output = [1,2]
    actual_output = Solution().topKFrequent(arr, k)
    if actual_output==expected_output:
        print("pass")
    else:
        print("fail")
        print(actual_output)