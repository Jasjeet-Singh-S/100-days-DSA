# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

class Solution:
    def activitySelection(self, start, finish):
        arr = list(zip(start, finish))
        arr.sort(key=lambda x: x[1])

        # at least one activity can be performed
        count = 1

        # index of last selected activity
        j = 0
        for i in range(1, len(arr)):
            # check if current activity starts after last activity ends
            if arr[i][0] > arr[j][1]:
                count += 1
                # update j
                j = i
        
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