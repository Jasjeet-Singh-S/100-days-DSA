class Solution:
    def countTriplets(self, sum, arr):
        count = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]<sum:
                        count+=1
                    else:
                        break
        return count