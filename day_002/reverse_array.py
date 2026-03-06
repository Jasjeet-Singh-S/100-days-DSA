class Solution:
    def reverseArray(self, arr):
        temp = 0
        lenght = len(arr)
        for i in range(int(lenght/2)):
            temp = arr[i]
            arr[i] = arr[-i-1]
            arr[-i-1] = temp
