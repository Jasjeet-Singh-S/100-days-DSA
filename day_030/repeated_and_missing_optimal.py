# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        expected_sum = (len(A)*((2*1)+(len(A)-1)*1))//2  # sum of AP formula
        expected_square_sum = (len(A)*(len(A)+1)*(2*len(A)+1))//6  # formula for sum of first n squares
        
        actual_sum = 0
        actual_square_sum = 0
        for i in range(len(A)):
            actual_sum += A[i]
        for i in range(len(A)):
            actual_square_sum += A[i]**2

        diff = expected_sum - actual_sum
        sq_diff = expected_square_sum - actual_square_sum
        sum = sq_diff/diff
        a = (sum+diff)//2
        b = (sum-diff)//2
        return [int(b),int(a)]
        


def main():
    input_1 = [1,3,4,5,5] 
    expected_output_1 = [3, 4]
    
    sol = Solution()

    actual_output_1 = sol.repeatedNumber(input_1)

    if expected_output_1==actual_output_1:
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(expected_output_1)


if __name__=="__main__":
    main()