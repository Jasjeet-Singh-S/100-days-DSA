class Solution:
    def maxSubArray(self, nums):
        max = -10**4
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if(sum>max):
                max = sum
            if(sum<=0):
                sum = 0
        return max


def main():
    arr_1 = [-2,1,-3,4,-1,2,1,-5,4]
    expected_result_1 = 6
    arr_2 = [1]
    expected_result_2 = 1
    arr_3 = [5,4,-1,7,8]
    expected_result_3 = 23

    solution = Solution()
    actual_result_1 = solution.maxSubArray(arr_1)    
    actual_result_2 = solution.maxSubArray(arr_2)
    actual_result_3 = solution.maxSubArray(arr_3)

    if(actual_result_1!=expected_result_1 or actual_result_2!=expected_result_2 or actual_result_3!=expected_result_3):
        print("fail")
        print(actual_result_1, actual_result_2, actual_result_3)
    else:
        print("pass")

if __name__=="__main__":
    main()