class Solution:
    def validateOp(self, a, b):
        # code here 
        stack = []
        j = 0

        for i in range(len(a)):
            stack.append(a[i])
            while stack and stack[-1]==b[j]:
                stack.pop()
                j+=1
            
        return j==len(a)
    
if __name__ == '__main__':
    a = [1, 2, 3]
    b = [2, 1, 3]

    print("true" if Solution().validateOp(a, b) else "false")        