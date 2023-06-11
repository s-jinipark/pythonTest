
# self
def DFS(L, sum):
    if L == N+1 : # 종료 조건
        print(sum)
        return
    else:
        # 두가지로 뻗는데
        if L+inp[L][0] <= N+1 :   # oops! 여기 처음에 등호를 < 로 해서.. <= 로 변경함
            DFS(L+inp[L][0], sum+inp[L][1])
        DFS(L+1, sum)

def solution():
    answer = 0
    # 하나씩 밀어
    inp.insert(0, [0,0])
    print(inp)
    # 1일 부터..(index 를 날짜로 사용하기 위해)
    DFS(1, 0)

    return answer

# N+1 에 휴가
N = 7

inp = [
    [4, 20],
    [2, 10],
    [3, 15],
    [3, 20],
    [2, 30],
    [2, 20],
    [1, 10]
]

re = solution()
print('re :', re)


