
# N x N 크기의 정사각형
# 가장 왼쪽 위 (1, 1) , 가장 오른쪽 아래 는 (N, N)

#####
class Solution:

    def three_in_time( self, N:int ) -> int:
        rtn = 0
        #tmp = ""
        for i in range(N+1) :
            for j in range(60):
                for k in range (60) :
                    tmp = str(i) + str(j) + str(k)
                    if "3" in tmp :
                        print(i, j, k )
                        rtn += 1

        return rtn



# def main():

#lst = ['R','R','R','U','D','D']
N = 5
#K = 3
sol = Solution()

print(sol.three_in_time( N))
