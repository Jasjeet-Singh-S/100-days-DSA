# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        arr = list(A)
        arr.sort()
        output = []
        i = 0
        # find repeated number
        for i in range(len(arr)-1):
            if arr[i+1]!=arr[i]+1 and arr[i+1]!=arr[i]+2:
                output.append(arr[i+1])
                break
            i+=1
        # find missing number 
        for i in range(len(arr)-1):
            if arr[i+1]==arr[i]+2:
                output.append(arr[i]+1)
        # edge cases
        if arr[0]!=1:
            output.append(1)
        if arr[len(arr)-1]!=len(arr):
            output.append(len(arr))
                
        return output


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