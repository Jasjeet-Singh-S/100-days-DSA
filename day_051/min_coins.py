class Solution:
    def findMin(self, n):
       denomination = [1,2,5,10]
       m = len(denomination)-1
       op = 0
       while True:
            if n-denomination[m]==0:
               return op+1
            elif n-denomination[m]>0:
               n = n-denomination[m]
               op += 1
            else:
                m-=1
            

if __name__=="__main__":
    n = 39
    expected_output = 6
    
    sol = Solution()
    
    actual_output = sol.findMin(n)

    if actual_output==expected_output:
        print("pass")
    else:
        print("fail")
        print(actual_output)