
# 1. N 에서 1 을 뺀다
# 2. N 을 K 로 나눈다

#####
class Solution:

    def till_1( self, N:int, K:int) -> int:
        rtn = 0
        tmp = N
        cnt = 0
        while tmp > 1 :
            if tmp%K == 0 :
                tmp = tmp/K
            else :
                tmp -= 1
            cnt += 1
        rtn = cnt
        return rtn



# def main():


N = 25
K = 3
sol = Solution()

print(sol.till_1(N, K))
