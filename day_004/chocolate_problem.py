class Solution:
    def findMinDiff(self, arr,M):
        arr = sorted(arr)
        diff = 10**9
        loc = 0
        for i in range(len(arr)-M+1):
            if(arr[i+M-1]-arr[i]<diff):
                diff = arr[i+M-1]-arr[i]
                loc = i

        return arr[loc+M-1]-arr[loc]

def main():
    arr_1 = [3, 4, 1, 9, 56, 7, 9, 12]
    m1 = 5
    expected_output_1 = 6

    arr_2 = [11, 13, 7, 5, 13, 12]
    m2 = 4
    expected_output_2 = 2

    solution = Solution()

    output_1 = solution.findMinDiff(arr_1, m1)
    output_2 = solution.findMinDiff(arr_2, m2)

    if output_1 != expected_output_1 or output_2 != expected_output_2:
        print("failed")
        print(output_1)
        print(output_2)
    else:
        print("pass")

if __name__=="__main__":
    main()