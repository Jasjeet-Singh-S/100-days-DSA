# Replace O with X

doing geeks for geeks https://www.geeksforgeeks.org/dsa/given-matrix-o-x-replace-o-x-surrounded-x/ problem and for some reason this solution works
```
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
```
but this doesnt 
```
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
            if visited[-1][col]==0 and grid[-1][col]=="O":
                self.dfs(-1, col, visited, grid, delrow, delcol)
        
        # traverse first and last col
        for row in range(rows):
            # first col
            if visited[row][0]==0 and grid[row][0]=="O":
                self.dfs(row, 0, visited, grid, delrow, delcol)
            # last col
            if visited[row][-1]==0 and grid[row][-1]=="O":
                self.dfs(row, -1, visited, grid, delrow, delcol)

        # traverse the whole matrix
        for row in range(rows):
            for col in range(cols):
                if visited[row][col]==0 and grid[row][col]=="O":
                    grid[row][col]="X"

        return grid
```
even though the only difference is that i use -1 to get to the last row or column instead of `rows-1` or `cols-1` in these lines `if visited[-1][col]==0 and grid[-1][col]=="O":` yet i get this output 
Possibly your code does not work correctly for multiple test-cases (TCs).

    The first test case where your code failed:
    Test Cases Passed: 
    7 /1120
    For Input : 
    4
    4
    X O X O
    O X X O
    X O X X
    O O O X
    Your Code's output is: 
    [[X, O, X, O],
    [O, X, X, O],
    [X, X, X, X],
    [O, O, O, X]]
    It's Correct output is: 
    [[X, O, X, O],
    [O, X, X, O],
    [X, O, X, X],
    [O, O, O, X]]
    Output Difference: 
    [[X, O, X, O],
    [O, X, X, O],
    [X, XO, X, X],
    [O, O, O, X]]

# What claude sonnet has to say about the situtatuon
## The Bug: `-1` as an Index Passed to DFS

The issue is subtle. Using `-1` works fine for the **boundary checks** (`if visited[-1][col]...`), but the problem is you're passing `-1` as the actual row/column index **into your DFS function**.

```python
self.dfs(-1, col, visited, grid, delrow, delcol)  # ← passing -1 as row
self.dfs(row, -1, visited, grid, delrow, delcol)  # ← passing -1 as col
```

Inside DFS, you're almost certainly doing bounds checking like:

```python
if row < 0 or row >= rows or col < 0 or col >= cols:
    return
```

When you pass `-1` as the starting row, this check **immediately triggers** (`row < 0` is `True`), so the DFS **returns without doing anything** — the border `O`s never get marked as visited.

Then in the final sweep, those unvisited `O`s on the last row/column get incorrectly flipped to `X`.

---

## Why the boundary *check* works but DFS doesn't

```python
grid[-1][col]   # Python interprets this as grid[rows-1][col] ✓ — works for reading
self.dfs(-1, col, ...)  # DFS receives -1 literally, fails bounds check ✗
```

Python's negative indexing is a language feature for **element access**, but your DFS treats indices as plain integers for arithmetic and comparison — it doesn't know `-1` means "last row."

---

## Fix

Just keep using `rows-1` and `cols-1` when calling DFS (as in your working solution), or convert before the call:

```python
if visited[rows-1][col]==0 and grid[rows-1][col]=="O":
    self.dfs(rows-1, col, visited, grid, delrow, delcol)  # ← explicit index
```

The working version is correct precisely because it passes the actual integer index, not `-1`.