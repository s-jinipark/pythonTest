
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

SIZE = 4

x = [0] * SIZE

def is_free(ix, iy) :
    for i in range(iy):
        if x[i]== ix or abs(x[i]-ix) == abs(i-iy):
            return False
    return True

def dfs(n) :    # 이게 queen()
    if n == SIZE :
        print(x)
        return
    for i in range(SIZE):
        if is_free(i, n) :   # 여기가 핵심
            x[n] = i  # 이게 퀸을 [n, i] 에 놓겠다는 의미
            dfs(n+1)

dfs(0)  # 0 부터 시작이야...

print('--------------------')

def is_free2(xi) :
    for i in range(xi): #인덱스가 행  x[n]값이 열
        if x[i]== x[xi] or abs(x[xi]-x[i]) == abs(xi -i): # 열이 같거나 대각선이 같으면 false
            return False
    return True

def dfs2(n) :    # 이게 queen()
    if n == SIZE :
        print(x)
        return
    # 각 행에 퀸 놓기
    for i in range(SIZE):  # i 는 열번호 0부터 SIZE 전까지 옮겨가면서 유망한곳 찾기
        x[n] = i  # 이게 퀸을 [n, i] 에 놓겠다는 의미
        if is_free2(n) :   # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행 - 여기가 핵심
            #x[n] = i    # => 여기 있을 경우 안됨
            dfs2(n+1)

dfs2(0)  # 0 부터 시작이야...

# 여기 참조 => https://sso-feeling.tistory.com/415
# 설명 + 그림 -> https://abcdefgh123123.tistory.com/330
