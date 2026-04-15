# https://www.geeksforgeeks.org/dsa/merging-intervals/
# i just sorted the matrix based off the first column and then merged the rows accordingly

class Solution:
    def mergeOverlap(self, arr):
        # Option 1: Sorts the original list in-place
        arr.sort(key=lambda x: x[0])

        i=0
        while i < len(arr)-1:
            if arr[i][1]>=arr[i+1][0]:
                x=arr.pop(i)
                y=arr.pop(i)  # i since after previous pop i+1 comes to i
                arr.insert(i, [x[0],max(x[1],y[1])])
            else:
                i+=1
                
        return arr