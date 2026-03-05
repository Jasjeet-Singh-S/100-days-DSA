import numpy as np

class Solution:
    def getMinMax(self, arr):
        min = 10**9
        max = 1
        for i in range(len(arr)):
            if arr[i]>max:
                max = arr[i]
            if arr[i]<min:
                min = arr[i]
        return [min, max]
            


def main():
    x = 10  # example size
    arr = np.random.randint(1, 10**9 + 1, size=x, dtype=np.int32)  # int32 is fine for 1e9
    print(arr)
    solution = Solution()
    sol = solution.getMinMax(arr)
    print(sol)

if __name__=="__main__":
    main()