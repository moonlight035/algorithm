from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        do = [[x, y]]
        while do:
            t = do.pop()
            next, mineNum = self.existMine(board,t)
            if mineNum == 0:
                board[t[0]][t[1]] = 'B'
                do.extend(next)
            else:
                board[t[0]][t[1]] = str(mineNum)
        return board


    def existMine(self, board: List[List[str]], click: List[int]):
        x, y = click
        lx, ly = len(board), len(board[0])
        next = []
        mineNum = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i < lx and j >= 0 and j < ly and board[i][j] == 'M':
                    mineNum += 1
                if i >= 0 and i < lx and j >= 0 and j < ly and board[i][j] == 'E':
                    next.append([i,j])
        return [next, mineNum]