import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # 1. Create a heap with the first k elements
        # This takes O(k)
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # 2. Process the rest of the numbers
        # This takes O((n-k) * log k)
        for i in range(k, len(nums)):
            # If the current number is bigger than the smallest in our top-k
            if nums[i] > min_heap[0]:
                # Remove the smallest and add the new bigger number
                heapq.heapreplace(min_heap, nums[i])
        
        # 3. The top of the min-heap is the kth largest element
        return min_heap[0]


def main():
    arr_1 = [3,2,1,5,6,4]
    k_1 = 2
    expected_output_1 = 5
    arr_2 = [3,2,3,1,2,4,5,5,6]
    k_2 = 4
    expected_output_2 = 4

    sol = Solution()

    actual_output_1 = sol.findKthLargest(arr_1, k_1)
    actual_output_2 = sol.findKthLargest(arr_2, k_2)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(expected_output_1)
        print(actual_output_2)
        print(expected_output_2)


if __name__=="__main__":
    main()