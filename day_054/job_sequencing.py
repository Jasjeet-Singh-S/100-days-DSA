# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

import heapq
    
class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = sorted(zip(profit, deadline), key=lambda x: -x[0])
        
        max_d = max(deadline)
        parent = list(range(max_d + 1))
        
        def find(x):  # what's the highest available slot that is ≤ d?"
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        total_profit = 0
        count = 0
        
        for p, d in jobs:
            avail = find(d)
            if avail != 0:
                total_profit += p
                count += 1
                parent[avail] = avail - 1  # link to previous slot
        
        return [count, total_profit]
    

if __name__=="__main__":
    deadline = [4, 1, 1, 1]
    profit = [20, 10, 40, 30]
    expected_output = [2,60]

    sol = Solution()
    actual_output = sol.jobSequencing(deadline, profit)
    if actual_output==expected_output:
        print("pass")
    else:
        print("fail")
        print(actual_output)