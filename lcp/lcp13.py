from typing import List, Tuple


class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        lx = len(maze)
        ly = len(maze[0])
        organ = []
        stone = []
        start = ()
        target = ()
        for i in range(lx):
            for j in range(ly):
                if maze[i][j] == 'M':
                    organ.append((i,j))
                if maze[i][j] == 'S':
                    start = (i,j)
                if maze[i][j] == 'T':
                    target = (i,j)
                if maze[i][j] == 'O':
                    stone.append((i,j))
        stone.append(target)
        dis = self.disToStone(maze,stone)

        if len(organ) == 0:
            return dis[-1][start[0]][start[1]]

        organDistance = [[-1]*(len(organ)+1) for _ in range(len(organ)+1)]
        for i in range(len(organ)+1):
            for j in range(i+1,len(organ)+1):
                left = organ[i-1] if i > 0 else start
                right = organ[j-1]
                min = -1
                for k in dis[:-1]:
                    if k[left[0]][left[1]] == -1 or k[right[0]][right[1]] == -1:
                        continue
                    distance = k[left[0]][left[1]] + k[right[0]][right[1]]
                    if min == -1 or distance < min:
                        min = distance
                if min == -1:
                    return -1
                organDistance[i][j] = organDistance[j][i] = min

        for i in organ:
            if dis[-1][i[0]][i[1]] == -1:
                return -1

        dp = [[-1]*len(organ) for _ in range((1<<len(organ)))]
        for i in range(len(organ)):
            dp[1<<i][i] = dis[-1][organ[i][0]][organ[i][1]]
        mask = 1
        while mask < (1 << len(organ)):
            for i in range(len(organ)):
                if (1<<i) != mask and (1<<i)&mask:
                    min = -1
                    for j in range(len(organ)):
                        if ((1<<j)&mask) and i != j:
                            if min == -1 or organDistance[i+1][j+1] + dp[mask - (1<<i)][j] < min:
                                min = organDistance[i+1][j+1] + dp[mask - (1<<i)][j]
                    dp[mask][i] = min
            mask += 1
        min = -1
        for i in range(len(organ)):
            if min == -1 or dp[(1<<len(organ))-1][i] + organDistance[0][i+1] < min:
                min = dp[(1<<len(organ))-1][i] + organDistance[0][i+1]
        return min


    def dd(self):
        mask = 1
        organ = []
        organDistance = []
        dp = [[]]
        while mask < (1 << len(organ)):
            a = mask
            while a:
                i = a&(-a)
                min = -1
                b = mask - i
                while b:
                    j = b&(-b)
                    if min == -1 or organDistance[i+1][j+1] + dp[mask - (1<<i)][j] < min:
                        min = organDistance[i+1][j+1] + dp[mask - (1<<i)][j]
                    b = b-j
                dp[mask][i] = min
                a = a - i
            mask += 1


    def disToStone(self, maze: List[str], stone: List[Tuple]) -> List[List[List[int]]]:
        lx = len(maze)
        ly = len(maze[0])
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        res = []
        for i in stone:
            next = [i]
            dis = [[-1]*ly for _ in range(lx)]
            dis[i[0]][i[1]] = 0
            while next:
                t = next.pop(0)
                for d in direction:
                    nextX, nextY = t[0] + d[0], t[1] + d[1]
                    if nextX >= 0 and nextX < lx and nextY >= 0 and nextY < ly \
                            and dis[nextX][nextY] == -1 and maze[nextX][nextY] != '#':
                        dis[nextX][nextY] = dis[t[0]][t[1]] + 1
                        next.append((nextX, nextY))
            res.append(dis)
        return res

    def dfs(self, maze: List[str], stone: List[Tuple]) -> List[List[List[int]]]:
        lx = len(maze)
        ly = len(maze[0])
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        res = []
        for i in stone:
            next = [i]
            dis = [[-1]*ly for _ in range(lx)]
            base = 1
            while next:
                temp = []
                for t in next:
                    for d in direction:
                        nextX, nextY = t[0] + d[0], t[1] + d[1]
                        if nextX >= 0 and nextX < lx and nextY >= 0 and nextY < ly \
                                and dis[nextX][nextY] == -1 and maze[nextX][nextY] != '#':
                            dis[nextX][nextY] = base
                            temp.append((nextX, nextY))
                base += 1
                next = temp
            res.append(dis)
        return res

s = Solution()
stone = [(89,72),(16,24)]
a = ["#...#...#.#...#.##...#......##........#...#.#.#......##......#.#......#.#..", "#.#...#....#.............#.##..#......#........##..#....#...........#......", "..#.......#.##.##..#...#..#...#.#...............#....#..#..##......#.#..#..", ".......#.#........#.....###..#........#...#..##.......#.....#.#............", ".##....#...#....#...##....................#..#.##...##..#.#.#.......#....#.", ".#.#.....#........#...............#....##..#......#...##.#..#...##..#.#.##.", ".#......#.##..#.#..#..........#.........#......####.....#.#.....####...#...", ".......#..........#.##.#..#..................#...#......#.#...#..#.#..##.#.", "..#....#..##.....#.##..........#.......#.......#..............#.##..#.##..#", "......#........##..#.#..#...#.#..##.........#..###.....#.#...#...#..#.####.", ".#...#.........##........###...#..#....#.....#....#....##......##....#...##", "..........#.#........................#...##....#.#.#.............##.#.#..#.", "....#..#.........#.......#..#.......#.##........####....##..##...#..#......", "..##.....#..#....#.........#...###.#.##.#..#.........#..#...##.#........#..", ".#...#...##.#.......................#..#.....#...................#..##...#.", "..........#............#...##............##....#..#.....#....#..#..........", "#....#.#...##..###......T.#.#...##.....#...#.......#.##......#...#..#..#.#.", "......#...............##........##.#.......#.......#.....#.#..#.........##.", ".#...##.....#......#.##.....#......#.#.......#...#...............##.##.....", "#..........#.#.###...#...#......#..##......#....#.......###..M.#.....##....", ".................#....###..#....#.##.#...##......##..................#.....", "................#...#.....#...#..#..#.#....#............#.#..#.......#...#.", "....#..#..........#...#######....#...#...#.....#####..#....#..#..#......#..", "...#.......#.....#....#......#..##..#.............#..#......##...##...#..#.", "........##..#.#.....#...#.....M#...#..#.#..##..##...#...#....#..........#.#", ".#....##...#.#.#.#..#..#.#.#..#...#.#.....#.......#......#..###..#..#.##...", "..#....#.##.......##.....###...#.####.......#......#..#...#.#....#....#.##.", "...#..#..#.....##.......#...........#.....#.#..#...#.#....##...#.##....#...", ".....#...#.#..#..#..#.......#..##...#.....#M.#.......#.....#.#......#.....#", "...#........#.....#...#....#..#..#.#.....##.#...##..........##......#.#..##", "..........#.##.#..###...#..###..##.....#.##....#....#...#..#..#..#...#...#.", "......##........###..#.#.#......#.........#.......#...#...#................", ".#.#......#........##...#................#.##.........####..#..##..#.#.#...", ".##.##.#.........#.....##.#.#......#..##.#..###......##.#..##.#.######...#.", "##.#...#...##.#.#..#......#...............#..................#......#.##..#", ".......#.#.##.#.#.##..#.#..#.##...#...........#...#....#..##.....#....#.#..", "#.............#......#.##....#...#.#..#.............###...............#....", "...##...#..#.........#.#.##.##..##..###.###..#....#........#..##....##.##..", ".#..#.#..#.#....####......#...#............................#.....#....##...", "......#..#...#...#.............#...#.........###........#..#..M....#.......", "..#.##..........#.......##.#......##..#.....#.....#...##......##..........#", "#...#.#.#.....##.#.....#....#...........##........#....#....#..##...#..#.#.", "...##....#...#...........##.#......##.....#.......##..#..........#.........", "..............#.....#..##..#.....#....##.....#.#.............#..###....#.#.", "...##...#....##.#.....#....#...##..#..#.#........##..##.......#...#..###...", "#....#.....#................#.....#.......##................###............", "....##.#....#...............#.......#......#...#...###............##..#.#..", ".###.###...#..#..#.#.............#..#..#.#..........#.....#....#.#.....#...", "#.....##.#......###.#..........#..#.........#...................#....###...", "#.###....##..#...#.#....M.......#.#..........#.........#....#####...#......", ".##.#...............##...#..........#...#..#..........#..##...#.#.#.....#..", ".#......#..#......##........#...#......#.#..#.#.....##.##.#..#....#.##...#.", "...#.#..##.........##.#........#.........#.##..####..##..#..#...#...##...#.", ".#.....#.............##....#..#...#...##..##..##.....##.....#.......#......", "##.#......#...##.........#.###...........#...#.#.......#...#.#..#..##...#..", ".................##.#....#.#..##..................#.##....###......#.......", "..#.#...#......#..###...#.#............#..........#.##..#..#.....#...#.....", ".##....##............#...#.....#.##.....#.#..#.#..##.##......#..........##.", "#.#.......###..####..##..##............##..#...#.#..................#.###.#", "....##.........#.#..#........#..#..##.#......###...#........#.....##..#....", "#...#...#...#.....#.#..#...#.##..................#.##...#.#..#.......#.....", "....#.##.#.###.......#..........#..###.....#....#.#.#.#......#.#..##.#.....", ".#..............##..#.#.........#.#....#S..#.....#.##....#.##...........#..", "..##......#..#.....#.#.#...#.#.....#.#..#####..###...##...#.....#...#.....#", "........#.##..#.##....#......#.##.#......#....#..#.......#.#.....#........#", "......#.....#...##....###.#...#..#..#.......#..#.#....##.#.....#..#.....#..", "..........#.#...#............#....##..###.......#........#..............#..", "..##...#..##.......##......................#.....#.##..#.#...#.....###.#...", "##............##.....#............#.#.....#..##...##..#...#........##......", "#....#....#.........M......#..#..#..#......#......###........#.#........#..", ".#.#..##...#.#...#.#....#.#....#......#.#..#........#............####......", "....#....#....#.#...#....#..#.#....M.....#...........#...#...##.#......#...", "......##...#....#....#..#.#.##.......#....##.#....#..#..#.#...###..##.##...", ".#......#..#.....#.........#....#.............#........##..##....#.....#.#.", ".#.##.##..#..##.##.#....#...#...........#.....#..##................#.##....", "#..#..###......##.##..##.##...............#.........#....##..#...#.#.#....#", "....#.#...##.#.#.......#.#...#....##..............#..##.......##..#..#.....", "...#.#.........##......#.....#..#.##..###..#..#.#........#......##..#.....#", "#.#.....##.##.......#.#.....#......#..##....#....#..#...........#.#..#.....", "...........##...#...#..#....#..##.....#..#...#.##..............#..##.....#.", "......M#.#.#.......##.##....#.#.#........#.##....#........#...###.......#..", "..........###........#......##...#.#...........#....#.##...#.#...#....#....", ".##.....#.......#...#.....#.....#..........#..#....##............#..#..#...", "...........#...#.#.#.#...#.#....#......#........#.#..#...#....#.#..........", ".##...#..#.###..#.........##....#..............#........#.#..#.##M.........", "###....#..#####..#..#..#...#.....#.#......#####.#.........##.#..#....#.#...", "...#..#.......#........#............##.#.#...#.#...#....###..#.............", "..#.#.#....#...#..#..#.#...#......#...###..#..#...#..##..##....#.......#...", "...#......#..##..#..#............###..........#........#...##..##..#....#..", "###........#..##.....#..##......##..#..#.......#..#.....................O..", "........###.#...#......#.......#....#.....#..#..#....##.##..##....#....#.#.", "##..##..##.....##......#....#.#....##.......##.#........##.#..#....####...#", "#..##....#.....##.#.....#.............#...##.#...#...#..#........#.##......", ".##.#.##...........#...........#.......#.##......##..#.......###..#..##...#", "..#........#....##.....#..#......##...##...#.#.#.#......#....#.#..#.....#..", "..#...##.....#.#.#..................#..#.....#..........#..#.M..#........#.", "..#.....##..#.........##...........##....#........#..M...#........#.#......", ".##.##.....#......................#..#.#...#.........#.....#...###....#.#..", "#.##.....#.....#........#.......##..###.........#.#....#.....#..#..##......", "......#.............##......######...#..#.##...#.##.##.....#.#..#.#.#...##."]
print(s.dfs(a,stone))
print(s.disToStone(a,stone))
print(s.minimalSteps(a))