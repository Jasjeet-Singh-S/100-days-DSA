import copy

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = copy.deepcopy(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                matrix[col][row] = matrix_copy[rows-1-row][col]


def main():
    mat_1 = [[1,2,3],[4,5,6],[7,8,9]]
    expected_output_1 = [[7,4,1],[8,5,2],[9,6,3]]
    mat_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    expected_output_2 = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    solution = Solution()

    solution.rotate(mat_1)
    solution.rotate(mat_2)

    if(mat_1==expected_output_1 and mat_2==expected_output_2):
        print("pass")
    else:
        print("fail")
        print(mat_1)
        print(expected_output_1)
        print(mat_2)
        print(expected_output_2)

if __name__=="__main__":
    main()