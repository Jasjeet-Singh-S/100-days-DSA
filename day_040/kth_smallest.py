# kth largest algo but with k set to len(arr)-k
# pretty easy

class Solution:
    def kthSmallest(self, arr, k):
        return self.quickSelect(arr, 0, len(arr) - 1, len(arr)-k)

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