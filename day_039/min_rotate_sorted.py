# i just use the quickselect algo from day 31 and set k = len(nums) and that change alone was enough to solve the entire problem 
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums):
        k = len(nums)
        # We use a helper so we don't have to slice the list
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums, left, right, k_idx):
        pivot = nums[right]
        p_index = left
        
        for i in range(left, right):
            # Partitioning for LARGEST (Greater than pivot goes left)
            if nums[i] > pivot:
                nums[i], nums[p_index] = nums[p_index], nums[i]
                p_index += 1
        
        nums[p_index], nums[right] = nums[right], nums[p_index]

        if p_index == k_idx:
            return nums[p_index]
        elif p_index < k_idx:
            # Search the right side
            return self.quickSelect(nums, p_index + 1, right, k_idx)
        else:
            # Search the left side
            return self.quickSelect(nums, left, p_index - 1, k_idx)

    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t