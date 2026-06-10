# https://www.geeksforgeeks.org/problems/pair-sum-in-a-sorted-and-rotated-array/1

class Solution:
    def pairInSortedRotated(self,arr, target):
        n = len(arr)
        min_idx = 0  # cant just use arr.index(min(arr))  # because that would return the first min instead of correct min like in the array in main function
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                min_idx = i + 1
                break
        max_idx = min_idx + n -1
        while min_idx%n != max_idx%n:
            if (arr[min_idx%n]+arr[max_idx%n])>target:
                max_idx -= 1
            elif (arr[min_idx%n]+arr[max_idx%n])<target:
                min_idx += 1
            elif (arr[min_idx%n]+arr[max_idx%n])==target:
                return True
        return False
    
if __name__=="__main__":
    arr = [1,5,7,9,1,1,1]
    sol = Solution()
    if sol.pairInSortedRotated(arr, 16):
        print("pass")
    else:
        print("fail")