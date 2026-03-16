class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        path = set()

        for r in range(rows):
            for c in range(cols):
                if(self.dfs(board, word, rows, cols, r, c, 0, path)):
                        return True
        return False

    def dfs(self, board, word, rows, cols, r, c, i, path):
        if i==len(word):
            return True
        if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] 
            or (r,c) in path):
            return False
        else:
            path.add((r,c))
            res = (self.dfs(board, word, rows, cols, r+1, c, i+1, path)) or (self.dfs(board, word, rows, cols, r, c+1, i+1, path)) or (self.dfs(board, word, rows, cols, r-1, c, i+1, path)) or (self.dfs(board, word, rows, cols, r, c-1, i+1, path))
            path.remove((r,c))
            return res



def main():
    board_1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word_1 = "ABCCED"
    expected_output_1 = True
    board_2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word_2 = "SEE"
    expected_output_2 = True
    board_3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word_3 = "ABCB"
    expected_output_3 = False

    solution = Solution()

    actual_output_1 = solution.exist(board_1, word_1)
    actual_output_2 = solution.exist(board_2, word_2)
    actual_output_3 = solution.exist(board_3, word_3)

    if(actual_output_1==expected_output_1 and actual_output_2==expected_output_2
       and actual_output_3==expected_output_3):
        print("pass")
    else:
        print("fail")
        print(actual_output_1)
        print(actual_output_2)
        print(actual_output_3)

if __name__ == "__main__":
    main()