class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        # code here
        sum_1 = sum(s1)
        sum_2 = sum(s2)
        sum_3 = sum(s3)

        top_1, top_2, top_3 = 0, 0, 0

        while True:
            if len(s1)==top_1 or len(s2)==top_2 or len(s3)==top_3:
                return 0

            if sum_1 == sum_2 == sum_3:
                return sum_1  # or 2 or 3

            if sum_1 >= sum_2 and sum_1 >= sum_3:
                sum_1 -= s1[top_1]
                top_1 += 1
            elif sum_2 >= sum_1 and sum_2 >= sum_3:
                sum_2 -= s2[top_2]
                top_2 += 1
            else:
                sum_3 -= s3[top_3]
                top_3 += 1