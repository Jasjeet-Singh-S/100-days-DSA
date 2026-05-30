# https://www.geeksforgeeks.org/problems/majority-element-1587115620/1

# this is the optimized version of the brute solution. The best solution is moores voting algo 
from typing import List

class Solution:
    def majorityElement(self, arr:List[int]):
        arr.sort()
        i = 0
        n = len(arr)
        prev = arr[0]
        count = 0
        target = n/2
        while i<n:
            if arr[i]==prev:
                count += 1
            else:
                count = 1
                prev = arr[i]
            if count>target:
                return arr[i]
            i += 1
        return -1



if __name__=="__main__":
    arr = [3,1,3,3,2]
    sol = Solution()
    if sol.majorityElement(arr)==3:
        print("pass")
    else:
        print("fail")