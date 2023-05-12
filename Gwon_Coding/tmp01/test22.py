
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
#
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 이거 N M 과 너무 비슷하다
# 일단 N이 4 개다 하면 N, M = 4, 4 와 같이 가고 가지치기 하는 걸로

N = 11
#s = []
s = [0] * N
cnt = 0

def is_free(x):
    # s 와 중복되면 여튼 안도는 거
    # if x not in s :
    #     return True
    # return False
    for i in range(x):
        # if s[i] == s[x] :
        #     return False
        # 대각선도 추가
        if s[x] == s[i] or abs(s[x]-s[i]) == x-i :
            return False
    return True

def dfs(x):
    global  cnt
    #if len(s) == N :    # 결국 4 개 채워지면 끝나는 ...
    if x == N :    #  채워져 있으니까 .. 변경
        print(s)
        cnt += 1
        return      # 이거 없으면 아래 부분이 else 로 가야 함

    #for i in range(1, N+1):
    for i in range(N):  # i 는 열번호 , y 란 소리
        s[x] = i  # 첫째줄(x) i(y) 에 놓겠다
        #if is_free(i) :
        if is_free(x):   # 여기가 x 여야 함
            #s.append(i)
            #s[x] = i    # 첫째줄(x) i(y) 에 놓겠다
            dfs(x+1)    # 이게 다음 줄 가는 거
            #s.pop()

    # 그냥 돌리면 256 개 나옴
    # 여기서 N M 의 card 1 개 뽑는게 -> 체스판 1줄이라고 보면 됨

dfs(0)

print(cnt)
