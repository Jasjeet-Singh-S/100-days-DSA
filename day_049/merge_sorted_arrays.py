# https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

# one solution can be just styart from right of a and left of b and compare elements and switch, then sort, but thats too easy and i wont be attempting that.

class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        length = n+m
        gap = length//2 + length%2
        while gap>0:
            left = 0
            right = left+gap
            while right<length:
                # array 1 and array 2
                if left<n and right>=n:
                    self.swapIfGreater(a, b, left, right-n)
                # array 2 and array 2
                elif left>=n:  # and right>n  # one is suffecient condition
                    self.swapIfGreater(b, b, left-n, right-n)
                # array 1 and array 1
                else:  # left<n and right<n
                    self.swapIfGreater(a, a, left, right)
                left += 1
                right += 1
            if gap==1:
                break
            else:
                gap = (gap//2) + (gap%2)
        

    def swapIfGreater(self, a, b, i, j):
        if a[i]>b[j]:
            t = a[i]
            a[i] = b[j]
            b[j] = t

if __name__=="__main__":
    sol = Solution()
    arr_1 = [2, 4, 7, 10]
    arr_2 = [2, 3]
    sol.mergeArrays(arr_1, arr_2)
    print(arr_1)
    print(arr_2)