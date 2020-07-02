from typing import List



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def merge(x:List[int],y:List[int],z:List[int]):
            res = []
            for i in x:
                if i in y and i in z:
                    res.append(i)
            return res

        length = len(board)
        x = [None]*length
        y = [None]*length
        z = [None]*length

        def predict(index:int,direction:int):
            res = list(range(1,length+1))
            if direction == 0:
                for j in range(length):
                    if board[index][j] != '.':
                        res.remove(int(board[index][j]))
                x[index] = res
            elif direction == 1:
                for i in range(length):
                    if board[i][index] != '.':
                        res.remove(int(board[i][index]))
                y[index] = res
            else:
                beginX = (index // 3) * 3
                beginY = (index - beginX) * 3
                for i in range(beginX,beginX+3):
                    for j in range(beginY, beginY+3):
                        if board[i][j] != '.':
                            res.remove(int(board[i][j]))
                z[index] = res
            return res


        t = {}
        start = []
        for i in range(length):
            for j in range(length):
                if board[i][j] == '.':
                    tempX = x[i]
                    if tempX is None:
                        tempX = predict(i,0)
                    tempY = y[j]
                    if tempY is None:
                        tempY = predict(j,1)
                    tempZ = z[(i//3)*3+j//3]
                    if tempZ is None:
                        tempZ = predict((i//3)*3+j//3,2)
                    temp = merge(tempX,tempY,tempZ)
                    t[(i, j)] = temp
                    if len(temp) == 1:
                        start.append((i,j,temp[0]))

        def goBack(back:List,val:int):
            for i in back:
                t[i].append(val)

        def handle(e,back):
            for i in range(length):
                if board[i][e[1]]=='.' and e[2] in t[(i,e[1])]:
                    t[(i,e[1])].remove(e[2])
                    back.append((i,e[1]))
                    if len(t[(i,e[1])]) == 1:
                        start.append((i,e[1],t[(i,e[1])][0]))
                    if len(t[(i, e[1])]) == 0:
                        return False


            for j in range(length):
                if board[e[0]][j]=='.' and e[2] in t[(e[0],j)]:
                    t[(e[0],j)] .remove(e[2])
                    back.append((e[0],j))
                    if len(t[(e[0],j)]) == 1:
                        start.append((e[0],j,t[(e[0],j)][0]))
                    if len(t[(e[0], j)]) == 0:
                        return False

            index = (e[0]//3)*3+e[1]//3
            beginX = (index//3)*3
            beginY = (index-beginX)*3
            for i in range(beginX,beginX+3):
                for j in range(beginY,beginY+3):
                    if i!=e[0] and j!=e[1] and board[i][j] == '.' and e[2] in t[(i,j)]:
                        t[(i,j)].remove(e[2])
                        back.append((i,j))
                        if len(t[(i,j)]) == 1:
                            start.append((i,j,t[(i,j)][0]))
                        if len(t[(i,j)]) == 0:
                            return False
            return True
        while start:
            e = start.pop()
            board[e[0]][e[1]] = str(e[2])
            handle(e,[])
            t.pop((e[0],e[1]))

        m = list(t.keys())
        def digui(index:int):
            if index == len(m):
                return True
            e = m[index]
            for i in t[e]:
                back = []
                board[e[0]][e[1]] = str(i)
                if not handle((e[0],e[1],i),back) or not digui(index+1):
                    board[e[0]][e[1]] = '.'
                    goBack(back,str(i))
                else:
                    return True
            return False

        digui(0)
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
x =[[".",".","9","7","4","8",".",".","."],
     ["7",".",".",".",".",".",".",".","."],
     [".","2",".","1",".","9",".",".","."],
     [".",".","7",".",".",".","2","4","."],
     [".","6","4",".","1",".","5","9","."],
     [".","9","8",".",".",".","3",".","."],
     [".",".",".","8",".","3",".","2","."],
     [".",".",".",".",".",".",".",".","6"],
     [".",".",".","2","7","5","9",".","."]]
s.solveSudoku(x)

for i in x:
    print(i)
print(s.isValidSudoku(x))
