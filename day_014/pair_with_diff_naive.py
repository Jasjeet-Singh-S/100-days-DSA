
from typing import List


class Solution:
    def findPair(self, arr, x):
        n = len(arr)
        
        # Compare each element with every other element
        for i in range(n):
            for j in range(i + 1, n):
                
                # Check if absolute difference matches target
                if abs(arr[i] - arr[j]) == x:
                    return True
        
        return False