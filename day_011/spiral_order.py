class Solution:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, cols-1
        top, bottom = 0, rows-1

        result = []
        while(top<=bottom and left<=right):
            # right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            if(top<=bottom):
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if(left<=right):
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


def main():
    matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
    expected_order_1 = [1,2,3,6,9,8,7,4,5]
    matrix_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    expected_order_2 = [1,2,3,4,8,12,11,10,9,5,6,7]

    solution = Solution()

    actual_order_1 = solution.spiralOrder(matrix_1)
    actual_order_2 = solution.spiralOrder(matrix_2)

    if(actual_order_1==expected_order_1 and actual_order_2==expected_order_2):
        print("pass")
    else:
        print("fail")
        print(actual_order_1)
        print(expected_order_1)
        print(actual_order_2)
        print(expected_order_2)

if __name__=="__main__":
    main()