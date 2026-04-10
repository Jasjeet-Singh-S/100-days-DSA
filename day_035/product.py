class Solution:
    def productExceptSelf(self, nums):
        product = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                product *= nums[i]

        if zeros>=2:
            return [0]*len(nums)

        result = [int(product)] * len(nums)

        if zeros==1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    result[i]=0
            return result
    
        for i in range(len(nums)):
            result[i] = int(result[i]/nums[i])
        return result


def main():
    arr_1 = [1,2,3,4]
    expected_output_1 = [24,12,8,6]
    arr_2 = [-1,1,0,-3,3]
    expected_output_2 = [0,0,9,0,0]

    sol = Solution()

    actual_output_1 = sol.productExceptSelf(arr_1)
    actual_output_2 = sol.productExceptSelf(arr_2)

    if(expected_output_1==actual_output_1 and expected_output_2==actual_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(expected_output_1)
        print(actual_output_2)
        print(expected_output_2)


if __name__=="__main__":
    main()