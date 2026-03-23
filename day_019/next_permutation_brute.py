class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = self.permute(nums)
        ans.sort()

        # Remove duplicate permutations when input has repeated values.
        unique_ans = []
        seen = set()
        for perm in ans:
            key = tuple(perm)
            if key not in seen:
                seen.add(key)
                unique_ans.append(perm)

        for i in range(len(unique_ans)):
            if unique_ans[i] == nums:
                if i == len(unique_ans) - 1:
                    return unique_ans[0]
                return unique_ans[i + 1]


    def recursion_permutation(self, nums, ds, ans, freq):
        if len(ds) == len(nums):
            ans.append(ds[:])
            return
        for i in range(len(nums)):
            if not freq[i]:
                freq[i] = True
                ds.append(nums[i])
                self.recursion_permutation(nums, ds, ans, freq)
                freq[i] = False
                ds.pop()

    def permute(self, nums):
        ds = []
        ans = []
        freq = [False] * len(nums)
        self.recursion_permutation(nums, ds, ans, freq)
        return ans



def main():
    nums_1 = [1,2,3]
    expected_output_1 = [1,3,2]
    nums_2 = [3,2,1]
    expected_output_2 = [1,2,3]
    nums_3 = [1,1,5]
    expected_output_3 = [1,5,1]

    solution = Solution()

    actual_output_1 = solution.nextPermutation(nums_1)
    actual_output_2 = solution.nextPermutation(nums_2)
    actual_output_3 = solution.nextPermutation(nums_3)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2 and actual_output_3==expected_output_3):
        print("pass")
    else:
        print(expected_output_1)
        print(actual_output_1)
        print(expected_output_2)
        print(actual_output_2)
        print(expected_output_3)
        print(actual_output_3)


if __name__=="__main__":
    main()