# watch striver

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                j = i+1
                k = n-1
                while j<k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum<0:
                        j += 1
                    elif sum>0:
                        k -= 1
                    else:
                        answer.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while nums[j]==nums[j-1] and j<k:
                            j += 1
                        while nums[k]==nums[k+1] and j<k:
                            k -= 1

        return answer