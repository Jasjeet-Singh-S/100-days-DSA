## Number of Islands
I basically took the word search code 
```class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        path = set()

        for r in range(rows):
            for c in range(cols):
                if(self.dfs(board, word, rows, cols, r, c, 0, path)):
                        return True
        return False

    def dfs(self, board, word, rows, cols, r, c, i, path):
        if i==len(word):
            return True
        if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] 
            or (r,c) in path):
            return False
        else:
            path.add((r,c))
            res = (self.dfs(board, word, rows, cols, r+1, c, i+1, path)) or (self.dfs(board, word, rows, cols, r, c+1, i+1, path)) or (self.dfs(board, word, rows, cols, r-1, c, i+1, path)) or (self.dfs(board, word, rows, cols, r, c-1, i+1, path))
            path.remove((r,c))
            return res
```
And tried to modify it since number of islands is also a DFS problem, the solution i cam up with by modifying word search is this 
```
class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        path = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if((r,c) not in path and self.dfs(grid, rows, cols, r, c, path)):
                        count += 1
        return count

    def dfs(self, grid, rows, cols, r, c, path):
        if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in path or grid[r][c]!="L"):
            return False
        else:
            path.add((r,c))
            res = (self.dfs(grid, rows, cols, r+1, c, path)) or (self.dfs(grid, rows, cols, r, c+1, path)) or (self.dfs(grid, rows, cols, r-1, c, path)) or (self.dfs(grid, rows, cols, r, c-1, path))
            path.remove((r,c))
            if res>=0:
                return True
            else:
                return False
```
But the issue with this was that it was counting number Ls in the matrix rather than the number of islands, and i couldnt get the logic right, so i had to get claude's help and this is the final solution
```
class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                # Only start DFS if it's land AND not visited
                if grid[r][c] == "L" and (r,c) not in visited:
                    self.dfs(grid, rows, cols, r, c, visited)
                    count += 1  # Increment AFTER exploring entire island
        return count

    def dfs(self, grid, rows, cols, r, c, visited):
        # Base cases
        if (r<0 or c<0 or r>=rows or c>=cols or 
            (r,c) in visited or grid[r][c] != "L"):
            return
        
        # Mark as visited
        visited.add((r,c))
        
        # Explore all 4 directions
        self.dfs(grid, rows, cols, r+1, c, visited)
        self.dfs(grid, rows, cols, r+1, c+1, visited)
        self.dfs(grid, rows, cols, r, c+1, visited)
        self.dfs(grid, rows, cols, r-1, c+1, visited)
        self.dfs(grid, rows, cols, r-1, c, visited)
        self.dfs(grid, rows, cols, r-1, c-1, visited)
        self.dfs(grid, rows, cols, r, c-1, visited)
        self.dfs(grid, rows, cols, r+1, c-1, visited)
```
Also made sure there are 8 directions to check instead of 4 like in the word problem 

## Permutation Pair Sum
This problem was super easy, just sort both arrays and compare descending and ascending corresponding value sums to K