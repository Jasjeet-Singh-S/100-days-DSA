import copy

class Solution:
    def findKthLargest(self, nums, k):
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


def main():
    arr_1 = [3,2,1,5,6,4]
    k_1 = 2
    expected_output_1 = 5
    arr_2 = [3,2,3,1,2,4,5,5,6]
    k_2 = 4
    expected_output_2 = 4

    sol = Solution()

    actual_output_1 = sol.findKthLargest(arr_1, k_1)
    actual_output_2 = sol.findKthLargest(arr_2, k_2)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(expected_output_1)
        print(actual_output_2)
        print(expected_output_2)


if __name__=="__main__":
    main()