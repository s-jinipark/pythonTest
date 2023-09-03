
##### 바둑이 승차(DFS)
def DFS(v, sum):
    global  Max
    if v == N :
        if sum > C :
            return
        else:
            print(sum)
            if Max < sum:
                Max =  sum
        #return
    else:
        DFS(v+1, sum)
        DFS(v+1, sum + inp[v])

def solution():
    answer = 0
    '''
    그렇다면, 4번과 똑같다
    
    '''
    DFS(0, 0)
    print('Max', Max)
    return answer

C = 259  # max 값이라고 보면됨
N = 5  # 바둑이 수

inp = [81, 58, 42, 33, 61]
Max = 0  # 해설에서는 -2147000000 (0 여섯개)

re = solution()
print(re)
#=> 242
print('====================')

