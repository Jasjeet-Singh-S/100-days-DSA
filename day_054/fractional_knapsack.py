# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n = len(val)
        items = sorted(
            [(val[i] / wt[i], wt[i]) for i in range(n)],
            key=lambda x: -x[0]
        )

        output = 0.0
        i = 0
        while capacity > 0 and i < n:
            density, weight = items[i]
            taken = min(capacity, weight)
            output += taken * density
            capacity -= taken
            i += 1

        return output


if __name__=="__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    capacity = 50
    expected_output = 240.0
    actual_output = Solution().fractionalKnapsack(val, wt, capacity)
    if actual_output==expected_output:
        print("pass")
    else:
        print("fail")
        print(expected_output)
        print(actual_output)