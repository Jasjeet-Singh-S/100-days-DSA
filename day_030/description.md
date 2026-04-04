# Repeated and Missing Number 
ok so the previous approach we used had to linear loops and a sort that makes it O(N*LogN) and we used O(N) space. What we want is O(N) time and O(1) space. For that we will use a clever approach as follows:
## Steps
- let the read only array be `arr_1=[1,2,3,....n]` in some unsorted manner
- let there be some expected array `arr_2=[1,2,3....n]` that is the actual correct array from 1 to n
- let the sum of the given array be `a=sum(arr_1)`
- let the sum of the expected array be `b=sum(arr_2)`
- let the sum of squares of the given array be `a_s=sum(elemwise(square(arr_1)))`
- let the sum of squares of the expected array be `b_s=sum(elemwise(square(arr_2)))`
- let the difference between the two be `diff=a-b`, this isolated the repeated number and missing number in the form of `repeated-missing`
- let the difference between the squares of two be `sq_diff=a_s-b_s`, this isolates the repeated number and missing number in the form of `repeated**2-missing**2`
- we can create a third equation by exploting the existing two equations: `repeated+missing=(repeated**2-missing**2)/(repeated-missing)`
- and then extract the missing and repeated number by solving the set of linear equations `repeated+missing=something` and `repeated-missing=something`
- in the end we return the value `[repeated, missing]`

# K'th largest element 
my first though was to sort the elements but the description pecifically says to try to not use sort to solve this [problem](https://leetcode.com/problems/kth-largest-element-in-an-array/) so i thought i would use the following appraoch 
```
class Solution:
    def findKthLargest(self, nums, k):
        k_largest = [0]
        for i in range(len(nums)):
            if nums[i]>k_largest[self.smallest(k_largest)]:
                k_largest.append(nums[i])
            if len(k_largest)>k:
                k_largest.pop(self.smallest(k_largest))
            
        return k_largest[self.smallest(k_largest)]
    
    def smallest(self, k_largest):
        index = 0
        for i in range(len(k_largest)):
            if k_largest[i]<k_largest[index]:
                index = i
        return index
```
here i basically maintain an array of k largest elements and then return the smallest out of those. Every time i find an element greater than the smallest element of k_largest i replace the smallest with this new element. But the time complexity of this is O(N.K) which can effectively end up being O(N^2) which is worse than O(NlogN) which is what sorting takes, so the next approach is to use min heaps which keeps the smallest element at the very top that makes the fidning smallest element complexity O(1) and inserting new element complexity O(logK) (not O(K) thanks to its tree structure. it's organized so that every "parent" is smaller than its two "children.")
```
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
```
Apparently there is an apprach that only takes O(N) time, i will attempt that tomorrow 