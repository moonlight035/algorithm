from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = []
        lx = len(board)
        ly = len(board[0])
        for i in range(lx):
            for j in range(ly):
                if board[i][j] == word[0]:
                    start.append((i,j))
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        def bound(x: int, y: int):
            if x >= 0 and x < lx and y >= 0 and y < ly:
                return True
            else:
                return False
        def search(now:tuple, status: List[List[bool]], index: int):
            if index==len(word):
                return True
            nowX,nowY = now
            for i in direction:
                nextX,nextY = nowX+i[0],nowY+i[1]
                if bound(nextX,nextY) and status[nextX][nextY] and word[index] == board[nextX][nextY]:
                    status[nextX][nextY] = False
                    if search((nextX,nextY), status, index+1):
                        return True
                    status[nextX][nextY] = True
            return False
        status = [[True]*ly for _ in range(lx)]
        for i in start:
            status[i[0]][i[1]]=False
            if search(i,status,1):
                return True
            status[i[0]][i[1]] = True
        return False
s = Solution()
print(s.exist([["a","a"]],"aaa"))