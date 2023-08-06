import sys

sys.setrecursionlimit(2001)


def solution(n, tolls):
    def proc(x, y):
        #print(x,y)
        if dp[x][y] > -1:
            return dp[x][y]
        if x == n - 1 and y == n - 1:
            ret = 0;
        elif x == n - 1:
            ret = proc(x, y + 1);
        elif y == n - 1:
            ret = proc(x + 1, y);
        else:
            ret = min(proc(x + 1, y), proc(x, y + 1))
        #dp[x][y] = ret
        dp[x][y] = ret + tolls[x][y]
        print('x,y,ret : ', x, y, ret)
        return dp[x][y]

    dp = [[-1 for j in range(1000)] for i in range(1000)]
    proc(0, 0)
    return dp[0][0]


n = 3
tolls = [[1, 2, 3], [0, 0, 0], [4, 5, 6]]

an = solution(n, tolls)
print(an)