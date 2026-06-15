# https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1

# check description.md for not BFS solution

from collections import deque
from typing import List

class Solution:
	def nearest(self, grid, source_value=1):
		"""
		Multi-source BFS on a grid.
		Computes shortest distance from each cell to the nearest source.

		Time Complexity:  O(m * n)
		Space Complexity: O(m * n)
		"""
		rows, cols = len(grid), len(grid[0])
		distance = [[-1] * cols for _ in range(rows)]
		visited = [[False] * cols for _ in range(rows)]
		queue = deque()

		# Initialize: enqueue all sources
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == source_value:
					queue.append((r, c))
					visited[r][c] = True
					distance[r][c] = 0

		directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

		# BFS expansion
		while queue:
			row, col = queue.popleft()

			for dr, dc in directions:
				nr, nc = row + dr, col + dc

				if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
					visited[nr][nc] = True
					distance[nr][nc] = distance[row][col] + 1
					queue.append((nr, nc))

		return distance
		
if __name__=="__main__":
	
	grid = [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
	expected_output = [[1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0]]
	actual_output = Solution().nearest(grid)
	if expected_output==actual_output:
		print("pass")
	else:
		print("fail")
		print(actual_output)