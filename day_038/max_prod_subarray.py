# i did this appraoch as recommended by striver, but honestly maybe just do kadane's, there are too many points of potential failure here that i might not be able to figure out in the interview
# https://www.youtube.com/watch?v=hnswaLJvr6g&t=753s
class Solution:
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]
        return self.maxProdNonNeg(nums)

    def maxProdNonNeg(self, nums):
        if not nums:
            return 0

        zeroes = self.countZeroes(nums)
        split_points = [-1] + zeroes + [len(nums)]
        candidates = [0]

        for s in range(len(split_points) - 1):
            segment = nums[split_points[s]+1 : split_points[s+1]]
            if not segment:
                continue
            seg_negs = self.countNegs(segment)

            if len(seg_negs) % 2 == 0:
                prod = 1
                for x in segment:
                    prod *= x
                candidates.append(prod)
            else:
                for drop in [seg_negs[0], seg_negs[-1]]:
                    left = segment[:drop]
                    right = segment[drop+1:]
                    for part in [left, right]:
                        if part:
                            prod = 1
                            for x in part:
                                prod *= x
                            candidates.append(prod)

        return max(candidates)

    def countNegs(self, nums):
        negs = []
        for i in range(len(nums)):
            if nums[i] < 0:
                negs.append(i)
        return negs

    def countZeroes(self, nums):
        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.append(i)
        return zeroes


def main():
    arr_1 = [2,3,-2,4]
    expected_output_1 = 6
    arr_2 = [-2]
    expected_output_2 = -2

    sol = Solution()

    actual_answer_1 = sol.maxProduct(arr_1)
    actual_answer_2 = sol.maxProduct(arr_2)

    if(expected_output_1==actual_answer_1 and expected_output_2==actual_answer_2):
        print("pass")
    else:
        print("fail")
        print(actual_answer_1)
        print(expected_output_1)
        print(actual_answer_2)
        print(expected_output_2)


if __name__=="__main__":
    main()