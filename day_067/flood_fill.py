# https://leetcode.com/problems/flood-fill/
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cell_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        self.bfs(image, visited, rows, cols, sr, sc, cell_color)

        for i in range(rows):
            for k in range(cols):
                if visited[i][k]==True:
                    image[i][k]=color

        return image

    def bfs(self, image, visited, rows, cols, row, col, color):
        if row<0 or col<0 or row>=rows or col>=cols or visited[row][col]==True or image[row][col]!=color:
            return

        visited[row][col] = True
        self.bfs(image, visited, rows, cols, row+1, col, color)
        self.bfs(image, visited, rows, cols, row, col+1, color)
        self.bfs(image, visited, rows, cols, row-1, col, color)
        self.bfs(image, visited, rows, cols, row, col-1, color)