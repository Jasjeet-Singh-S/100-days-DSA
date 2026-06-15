# Distance of nearest cell having 1

## BFS at each 0
I was thinking of this approach then i had trouble implementing BFS and also claude told me this has a time complexity of `O(n²·m²)

## Manhattan distance
I came up with this approach myself but apparently its called the manhattan approach by calculating distance using `min(distance, abs(xi-x)+abs(yi-y))` since 4 neighbour distance is being used and calulate minimum of that against all ones

```
class Solution:
    def nearest(self, grid):
 		distances = copy.deepcopy(grid)
 		ones = []
 		n = len(grid)
 		m = len(grid[0])
 		for i in range(n):
 			for k in range(m):
 				if grid[i][k]==1:
 					distances[i][k]=0
 					ones.append([i, k])
 		for x in range(n):
 			for y in range(m):
 				if grid[x][y]==0:
 					distance = 10000
 					for one in ones:
 						xi, yi = one
 						distance = min(distance, abs(xi-x)+abs(yi-y))
 						if distance==1:
 							break  # distance cant get any less than 1 so we can stop checking
 					distances[x][y] = distance
 		return distances
```
the reason this didnt work is because it has a time complexity of `O(n.m.k)` which gfg did not accept

## Multi source BFS
this is the approach gfg wanted me to use i guess as it has a time complexity of `O(n.m)`. I copied it from https://algomaster.io/learn/dsa/multi-source-bfs good place and it also comes with the explanation.