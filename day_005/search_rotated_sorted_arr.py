class Solution:
    
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # check if left half is sorted
            elif nums[mid] >= nums[left]:
                # search for target
                if(target>=nums[left] and target<nums[mid]):
                    right = mid-1
                else:
                    left = mid+1
            else:
                # similar pattern here
                if(target>nums[mid] and target<=nums[right]):
                    left = mid+1
                else:
                    right = mid-1
        return -1  # Target not found




def main():
    arr = [4,5,6,7,0,1,2]
    
    targ_1 = 0
    expected_output_1 = 4
    targ_2 = 3
    expected_output_2 = -1

    solution = Solution()

    actual_output_1 = solution.search(arr, targ_1)
    actual_output_2 = solution.search(arr, targ_2)

    if actual_output_1 != expected_output_1 or actual_output_2 != expected_output_2:
        print("fail")
        print(actual_output_1, actual_output_2)
    else:
        print("pass")

if __name__=="__main__":
    main()