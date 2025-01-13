
# 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서
# K 번을 초과하여 더해질 수 없는 것이 이 법칙의 특징

#####
class Solution:

    def big_number1( self, lst:list, N:int, M:int, K:int) -> int:
        rtn = 0
        print(lst)
        # 가장 큰 수
        lst.sort(reverse=True)
        print(lst)
        chng = 0
        for i in range( M ) :
            print(int( i/K) )
            rtn += lst[int( i/K)]
        return rtn

    # 위 .. 문제 잘못 이해
    def big_number2( self, lst:list, N:int, M:int, K:int) -> int:
        rtn = 0
        print(lst)
        # 가장 큰 수
        lst.sort(reverse=True)
        print(lst)
        
        tmp = []
        for i in range( K ) :
            #print(int( i/K) )
            tmp.append(lst[0])  # 가장 큰 수 최대 나온 뒤
        tmp.append(lst[1]) # 두번째 큰 수 => 다시 큰 수
        print(tmp)

        for i in range( M ) :
            print(int( i%(K+1)) )
            rtn += tmp[int( i%(K+1))]
        return rtn

# def main():
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때
lst = [2,4,5,4,6]
N = 5
M = 8
K = 3
sol = Solution()

print(sol.big_number2(lst, N, M, K))
