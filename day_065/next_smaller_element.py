# https://www.geeksforgeeks.org/problems/immediate-smaller-element1142/1
class Solution:
    def nextSmallerEle(self, arr):
        n = len(arr)
        stack = []
        larger = [-1] * n

        for i in range(n):
            while stack and arr[i]<arr[stack[-1]]:  # basically next greater element problem but i just changed the sign here
                larger[stack.pop()] = arr[i]
            
            stack.append(i)
        
        return larger