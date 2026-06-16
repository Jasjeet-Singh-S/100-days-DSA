# https://www.geeksforgeeks.org/problems/minimum-sum4058/1

class Solution:
    def minSum(self, arr):
        arr.sort()
        num_1 = []
        num_2 = []
        i = 0
        while i<len(arr):
            num_1.append(str(arr[i]))
            if i+1<len(arr):
                num_2.append(str(arr[i+1]))
            i+=2
        num_1 = [int("".join(num_1))]
        num_2 = [int("".join(num_2))]
        return str(num_1[0]+num_2[0])
        


if __name__=="__main__":
    arr = [6, 8, 4, 5, 2, 3]
    if Solution().minSum(arr)=="604":
        print("pass")
    else:
        print("fail")
        print(Solution().minSum(arr))