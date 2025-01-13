
# N x N 크기의 정사각형
# 가장 왼쪽 위 (1, 1) , 가장 오른쪽 아래 는 (N, N)

#####
class Solution:

    def up_down( self, lst:list, N:int ) -> str:
        rtn = ""
        loc = [1,1]
        for ch in lst :
            print(ch)
            if ch == 'R' :
                if loc[1]+1 <= N : 
                    loc[1] +=1
            elif ch == 'U' :
               if loc[0]-1 >= 1 : 
                    loc[0] -=1
            elif ch == 'D' :
               if loc[0]+1 <= N : 
                    loc[0] +=1
            elif ch == 'L' :
               if loc[1]-1 >= 1 : 
                    loc[1] -=1
        rtn = str(loc[0]) + " " + str(loc[1])
        return rtn



# def main():

lst = ['R','R','R','U','D','D']
N = 5
#K = 3
sol = Solution()

print(sol.up_down(lst, N))
