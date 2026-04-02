class Solution:
    def maxProfit(self, prices):
        delta = []
        for i in range(len(prices)-1):
            delta.append(prices[i+1]-prices[i])
            
        max_so_far = 0
        current_sum = 0
        for i in range(len(delta)):
            current_sum += delta[i]
            if(current_sum>max_so_far):
                max_so_far = current_sum
            if(current_sum<=0):
                current_sum = 0

        return max_so_far


def main():
    prices_1 = [7,1,5,3,6,4]
    expected_output_1 = 5
    prices_2 = [7,6,4,3,1]
    expected_output_2 = 0

    sol = Solution()

    actual_output_1 = sol.maxProfit(prices_1)
    actual_output_2 = sol.maxProfit(prices_2)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(actual_output_2)


if __name__=="__main__":
    main()