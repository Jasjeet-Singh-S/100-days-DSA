# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

import heapq

class Solution:
    def activitySelection(self, start, finish):
        count = 0 
        pq = []
        for i in range(len(start)):
            heapq.heappush(pq, (finish[i], start[i]))
        
        finish_time = -1
        
        while pq:
            activity = heapq.heappop(pq)
            if activity[1]>finish_time:
                finish_time = activity[0]
                count += 1
        
        return count

if __name__=="__main__":
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    expected_output = 4

    sol = Solution()
    actual_output = sol.activitySelection(start, end)
    if actual_output==expected_output:
        print("pass")
    else:
        print("fail")
        print(actual_output)