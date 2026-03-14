class Solution:
    def setZeroes(self, matrix) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_positions = []
        
        # First, find all positions with 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_positions.append((row, col))
        
        # Then, set rows and columns to 0
        for row, col in zero_positions:
            for c in range(cols):
                matrix[row][c] = 0
            for r in range(rows):
                matrix[r][col] = 0


def main():
    matrix_1 = [[1,1,1],[1,0,1],[1,1,1]]
    excepted_output_1 = [[1,0,1],[0,0,0],[1,0,1]]
    matrix_2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected_output_2 = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    solution = Solution()

    solution.setZeroes(matrix_1)
    solution.setZeroes(matrix_2)

    if(matrix_1==excepted_output_1 and matrix_2==expected_output_2):
        print("pass")
    else:
        print("fail")

if __name__ == "__main__":
    main()