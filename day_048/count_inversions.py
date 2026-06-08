# https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
# this is O(N2) answer
# class Solution:
#     def inversionCount(self, arr):
#         pairs = 0
#         start = 0 
#         for i in range(len(arr)):
#             end = len(arr)-1
#             for _ in range(len(arr)-start-1):
#                 if arr[start]>arr[end]:
#                     pairs+=1
#                     end-=1
#                 else:
#                     end-=1
#             start += 1
#         return pairs

# this approach does not work for multiple duplicate elements
# import copy

# class Solution:
#     def inversionCount(self, arr):
#         pairs = 0
#         arr_copy = copy.deepcopy(arr)
#         arr_copy.sort()
#         for i in range(len(arr)):
#             index = arr_copy.index(arr[i])
#             if i-index>0:
#                 pairs += i-index
#         return pairs
class Solution:
    def __init__(self):
        self.count = 0    

    def inversionCount(self, arr):
        self.count = 0
        n = len(arr)
        self.mergeSort(arr, 0, n-1)
        return self.count

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                self.count += n1-i  # basically merge sort but this line is added thats all
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)

if __name__=="__main__":
    sol = Solution()
    arr = [2, 4, 1, 3, 5]
    arr_2 = [10,10,1]
    expected_output = 3
    expected_output_2 = 2
    actual_output = sol.inversionCount(arr)
    actual_output_2 = sol.inversionCount(arr_2)
    if expected_output==actual_output and expected_output_2==actual_output_2:
        print("pass")
    else:
        print("fail")
        print(actual_output)
        print(actual_output_2)