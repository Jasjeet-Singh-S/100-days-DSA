class Solution:
    def ratInMaze(self, maze):
        answer = []
        n_rows = len(maze)
        n_cols = len(maze[0])
        visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]
        path = ""
        self.helper(maze, 0, 0, path, answer, visited)
        return answer

    def helper(self, maze, r, c, path, answer, visited):
        if r<0 or r>len(maze)-1 or c<0 or c>len(maze[0])-1 or maze[r][c]==0 or visited[r][c]==True:
            return
        if r==len(maze)-1 and c==len(maze[0])-1:
            answer.append(path)
            return
        visited[r][c] = True
        # down
        self.helper(maze, r+1, c, path+"D", answer, visited)
        # left
        self.helper(maze, r, c-1, path+"L", answer, visited)
        # right
        self.helper(maze, r, c+1, path+"R", answer, visited)
        # up
        self.helper(maze, r-1, c, path+"U", answer, visited)
        visited[r][c] = False


if __name__=="__main__":
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    output = ["DDRDRR", "DRDDRR"]
    sol = Solution()
    if sol.ratInMaze(maze)==output:
        print("pass")
    else:
        print("fail")