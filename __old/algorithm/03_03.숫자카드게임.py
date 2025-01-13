
# 먼저 행 선택
# 가장 숫자가 낮은 카드 뽑는다
# 최종적으로 가잔 높은 숫자의 카드를 뽑을 수 있도록..

#####
class Solution:

    def number_card_bk1( self, lst:list, N:int, M:int) -> int:
        rtn = 0
        for i in range(N) :
            lst[i].sort()
        
        max = 0
        for i in range(N) :
            print(lst[i])
            if max < lst[i][0] :
                max = lst[i][0]
        rtn = max
        return rtn

    def number_card( self, lst:list, N:int, M:int) -> int:
        rtn = 0
        max = 0
        for i in range(N) :
            print(min(lst[i]))
            tmp = min(lst[i])
            if max < tmp :
                max = tmp
        rtn = max                
        return rtn


# def main():

# lst = [[3,1,2], [4,1,4], [2,2,2]]
# N = 3
# M = 3
lst = [[7,3,1,8], [3,3,3,4] ]
N = 2
M = 4
sol = Solution()

print(sol.number_card(lst, N, M))
