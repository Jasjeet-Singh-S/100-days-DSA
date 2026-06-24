# https://www.geeksforgeeks.org/problems/combination-sum-1587115620/1


class Solution:
    def targetSumComb(self, arr, target):
        arr.sort()  # guarantees non-decreasing order, makes duplicates structurally impossible
        combinations = []
        self.backtracker(arr, target, [], combinations, 0)
        return combinations

    def backtracker(self, arr, target, combination, combinations, index):
        for i in range(index, len(arr)):
            integer = arr[i]
            current_sum = sum(combination) + integer
            if current_sum == target:
                combinations.append(combination + [integer])  # snapshot for storage only
                # no need to pop because we didnt actually modify the orignal combination list in the above line, we created a new modified list instead
            elif current_sum < target:
                combination.append(integer)
                self.backtracker(arr, target, combination, combinations, i)
                combination.pop()  # undo — backtrack to explore next branch
            else:
                break  # arr is sorted, all further elements will also exceed target

if __name__=="__main__":
    arr = [1, 2, 3]
    targ = 5
    output = Solution().targetSumComb(arr, targ)
    print(output)