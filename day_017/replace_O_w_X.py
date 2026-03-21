class Solution:
    def fill(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        # traverse first and last row
        for col in range(cols):
            # first row
            if visited[0][col]==0 and grid[0][col]=="O":
                self.dfs(0, col, visited, grid, delrow, delcol)
            # last row
            if visited[rows-1][col]==0 and grid[rows-1][col]=="O":
                self.dfs(rows-1, col, visited, grid, delrow, delcol)

        # traverse first and last col
        for row in range(rows):
            # first col
            if visited[row][0]==0 and grid[row][0]=="O":
                self.dfs(row, 0, visited, grid, delrow, delcol)
            # last col
            if visited[row][cols-1]==0 and grid[row][cols-1]=="O":
                self.dfs(row, cols-1, visited, grid, delrow, delcol)

        # traverse the whole matrix
        for row in range(rows):
            for col in range(cols):
                if visited[row][col]==0 and grid[row][col]=="O":
                    grid[row][col]="X"

        return grid

    def dfs(self, i, j, visited, grid, delrow, delcol):
        # mark the current node as visited
        visited[i][j] = 1
        row = len(grid)
        col = len(grid[0])

        # check for top, right, bottom and left
        for direction in range(4):
            ni = i + delrow[direction]
            nj = j + delcol[direction]
            if(0<=ni<row and 0<=nj<col and visited[ni][nj]==0 and grid[ni][nj]=="O"):
                self.dfs(ni, nj, visited, grid, delrow, delcol)


def main():
    grid_1 = [['X', 'X', 'X', 'X'], 
            ['X', 'O', 'X', 'X'], 
            ['X', 'O', 'O', 'X'], 
            ['X', 'O', 'X', 'X'], 
            ['X', 'X', 'O', 'O']]
    expected_output_1 = [['X', 'X', 'X', 'X'], 
                        ['X', 'X', 'X', 'X'], 
                        ['X', 'X', 'X', 'X'], 
                        ['X', 'X', 'X', 'X'], 
                        ['X', 'X', 'O', 'O']]
    grid_2 = [['X', 'O', 'X', 'X'], 
            ['X', 'O', 'X', 'X'], 
            ['X', 'O', 'O', 'X'], 
            ['X', 'O', 'X', 'X'], 
            ['X', 'X', 'O', 'O']]
    expected_output_2 = [['X', 'O', 'X', 'X'], 
                        ['X', 'O', 'X', 'X'], 
                        ['X', 'O', 'O', 'X'], 
                        ['X', 'O', 'X', 'X'], 
                        ['X', 'X', 'O', 'O']]
    grid_3 = [['X', 'X', 'X'], 
            ['X', 'O', 'X'], 
            ['X', 'X', 'X']]
    expected_output_3 = [['X', 'X', 'X'], 
                        ['X', 'X', 'X'], 
                        ['X', 'X', 'X']]
    
    solution = Solution()

    actual_output_1 = solution.fill(grid_1)
    actual_output_2 = solution.fill(grid_2)
    actual_output_3 = solution.fill(grid_3)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2 and actual_output_3==expected_output_3):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(expected_output_1)
        print(actual_output_2)
        print(expected_output_2)
        print(actual_output_3)
        print(expected_output_3)


if __name__=="__main__":
    main()