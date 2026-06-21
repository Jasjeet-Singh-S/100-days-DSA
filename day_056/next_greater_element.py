class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        stack = []
        larger = [-1] * n

        for i in range(n):
            while stack and arr[i]>arr[stack[-1]]:
                larger[stack.pop()] = arr[i]
            
            stack.append(i)
        
        return larger

if __name__=="__main__":
    arr = [1, 3, 2, 4]
    expected_output = [3, 4, 4, -1]
    actual_output = Solution().nextLargerElement(arr)
    if actual_output==expected_output:
        print("pass")
    else:
        print("fail")
        print(actual_output)