from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        x = [[None]*length for _ in range(length)]
        y = [[None]*length for _ in range(length)]
        z = [[None]*length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                if board[i][j] == '.':
                    continue
                temp = int(board[i][j])-1
                if x[i][temp] is not None:
                    return False
                else:
                    x[i][temp] = True
                if y[j][temp] is not None:
                    return False
                else:
                    y[j][temp] = True
                if z[(i//3)*3+j//3][temp] is not None:
                    return False
                else:
                    z[(i//3)*3+j//3][temp] = True
        return True

s = Solution()
# print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."],
#                        ["6",".",".","1","9","5",".",".","."],
#                        [".","9","8",".",".",".",".","6","."],
#                        ["8",".",".",".","6",".",".",".","3"],
#                        ["4",".",".","8",".","3",".",".","1"],
#                        ["7",".",".",".","2",".",".",".","6"],
#                        [".","6",".",".",".",".","2","8","."],
#                        [".",".",".","4","1","9",".",".","5"],
#                        [".",".",".",".","8",".",".","7","9"]]))
print(s.isValidSudoku([[".","8","7","6","5","4","3","2","1"],
                       ["2",".",".",".",".",".",".",".","."],
                       ["3",".",".",".",".",".",".",".","."],
                       ["4",".",".",".",".",".",".",".","."],
                       ["5",".",".",".",".",".",".",".","."],
                       ["6",".",".",".",".",".",".",".","."],
                       ["7",".",".",".",".",".",".",".","."],
                       ["8",".",".",".",".",".",".",".","."],
                       ["9",".",".",".",".",".",".",".","."]]))
