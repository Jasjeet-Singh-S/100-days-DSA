# https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

class Solution:
    def celebrity(self, mat):
        stack = []
        n = len(mat)

        for i in range(n):
            stack.append(i)

        while len(stack)>1:
            i = stack.pop()
            j = stack.pop()

            if mat[i][j]==0:
                stack.append(i)
            else:
                stack.append(j)

        celeb = stack.pop()

        for i in range(n):
            if (i!=celeb) and (mat[i][celeb]==0 or mat[celeb][i]==1):
                return -1

        return celeb