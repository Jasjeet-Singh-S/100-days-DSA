# https://www.geeksforgeeks.org/dsa/ceiling-in-a-sorted-array/

class Solution:
    def findCeil(self, arr, x):
        for i in range(len(arr)):
            if arr[i]>=x:
                return i
        return -1