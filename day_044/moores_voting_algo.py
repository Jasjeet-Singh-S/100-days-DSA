# https://www.geeksforgeeks.org/problems/majority-element-1587115620/1

# most optimized approach

class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        candidate = -1
        votes = 0
        
        # Finding majority candidate
        for i in range (n):
            if (votes == 0):
                candidate = arr[i]
                votes = 1
            else:
                if (arr[i] == candidate):
                    votes += 1
                else:
                    votes -= 1
        count = 0
        
        # Checking if majority candidate occurs more than n/2
        # times
        for i in range (n):
            if (arr[i] == candidate):
                count += 1
                
        if (count > n // 2):
            return candidate
        else:
            return -1



if __name__=="__main__":
    arr = [17, 19, 9, 5, 3, 6, 17, 7, 18, 16, 18, 11, 3, 15, 2]
    sol = Solution()
    if sol.majorityElement(arr)==-1:
        print("pass")
    else:
        print("fail")