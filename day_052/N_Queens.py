# https://www.geeksforgeeks.org/problems/n-queen-problem0315/1

class Solution:
    def is_safe(self, mat, row, col):
        n = len(mat)

        # Check column on upper side
        for i in range(row):
            if mat[i][col]:
                return False
            
        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if mat[i][j]:
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1 # Fixed starting point
        while i >= 0 and j < n:
            if mat[i][j]:
                return False
            i -= 1
            j += 1

        return True
    
    def place_queens(self, row, mat, result):
        n = len(mat)

        if row == n:
            ans = []
            for i in range(n):
                for j in range(n):
                    if mat[i][j]:
                        ans.append(j + 1)
            result.append(ans)
            return
        
        for col in range(n):
            if self.is_safe(mat, row, col):
                mat[row][col] = 1
                self.place_queens(row + 1, mat, result)
                mat[row][col] = 0 

    def nQueen(self, n):
        mat = [[0] * n for _ in range(n)]
        result = []
        self.place_queens(0, mat, result)
        return result

if __name__=="__main__":
    n = 4
    result = Solution().nQueen(n)
    for ans in result:
        print(" ".join(map(str, ans)))
