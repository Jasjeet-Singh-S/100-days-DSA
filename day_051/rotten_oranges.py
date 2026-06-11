# https://www.geeksforgeeks.org/problems/rotten-oranges2536/1
# ok so my intuition was that we can do multiple passes of rotting the tomatoes and then count the number of passes to calculate time but thta is apparently 
# a O((NxM)^2 solution but we can apparently do it in O(NxM) with queues and BFS which is what ill be attempting here instead of my initial intuition.

class Solution:
	def orangesRot(self, mat):
		n = len(mat)
		m = len(mat[0])
		
		queue = []  # will store [row, col, time]
		visited = [[False for _ in range(m)] for _ in range(n)]
		
		for i in range(n):
			for j in range(m):
				if mat[i][j]==2:
					queue.append([i,j,0])
					visited[i][j]=True
		
		time = 0
		del_row = [-1,0,1,0]
		del_col = [0,-1,0,1]
		
		while queue:
			value = queue.pop(0)
			row = value[0]
			col = value[1]
			t = value[2]
			time = max(t, time)
			
			for i in range(4):
				nrow = row+del_row[i]
				ncol = col+del_col[i]
				
				if 0<=nrow<n and 0<=ncol<m and not visited[nrow][ncol] and mat[nrow][ncol]==1:
					queue.append([nrow, ncol, t+1])
					visited[nrow][ncol]=True

		for i in range(n):
			for j in range(m):
				if visited[i][j]==False and mat[i][j]==1:
					return -1
		return time
		
	
if __name__=="__main__":
	mat = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
	expected_output = 2
	sol = Solution()
	actual_output = sol.orangesRot(mat)
	if expected_output==actual_output:
		print("pass")
	else:
		print("fail")
		print(actual_output)