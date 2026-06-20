# https://www.geeksforgeeks.org/problems/minimum-sum-of-absolute-differences-of-pairs/1

class Solution:
    def findMinSum(self, a, b):
        # code here
        a.sort()
        b.sort()
        sum = 0
        for i in range(len(a)):
            sum += abs(a[i]-b[i])
        return sum