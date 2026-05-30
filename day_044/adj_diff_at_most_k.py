# https://www.geeksforgeeks.org/problems/searching-in-an-array-where-adjacent-differ-by-at-most-k0456/1
# technically i can do the optimized sol, but that too is O(N) and the question is not intersting enough so im not going to

class Solution:
    def findStepKeyIndex(self, arr, k, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1


if __name__=="__main__":
    arr = [4, 5, 6, 7, 6]
    k = 1
    x = 6

    sol = Solution()

    output = sol.findStepKeyIndex(arr, k, x)

    print(output)