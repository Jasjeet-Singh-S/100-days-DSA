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


def main():
    grid_1 = [['L', 'L', 'W', 'W', 'W'], 
                ['W', 'L', 'W', 'W', 'L'], 
                ['L', 'W', 'W', 'L', 'L'], 
                ['W', 'W', 'W', 'W', 'W'], 
                ['L', 'W', 'L', 'L', 'W']]
    expected_output_1 = 4
    grid_2 = [['W', 'L', 'L', 'L', 'W', 'W', 'W'], 
              ['W', 'W', 'L', 'L', 'W', 'L', 'W']]
    expected_output_2 = 2

    solution = Solution()

    actual_output_1 = solution.numIslands(grid_1)
    actual_output_2 = solution.numIslands(grid_2)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(actual_output_2)


if __name__=="__main__":
    main()