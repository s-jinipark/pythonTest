

# N-Queen

N = 4
s = [0] * 4

def is_free(ix, iy):
    # x, y 인덱스가 오면 chk
    for i in range(iy):  # iy 까지 -> 중요...
        if s[i] == ix  or  abs (s[i] - ix) == abs(i - iy) :
            return False
    return True

'''
s 가 [0,1,0,0] 이라면 0-1 = -1 과 0-1  = -1 을 비교한다는 말
[0,0] 과 [1,1] 비교 되는 상황 
'''

def dfs(n):
    if n==N :
        print(s)
        return

    for i in range(N):  # 말 4개를 놓을 예정
        #print(i)
        #s[n] = i
        if is_free(i, n) :  # 다음칸 간다는게 결국 y 늘어나는 거
            s[n] = i
            dfs(n+1)
dfs(0)

# 그냥 돌리면 256 개
# 같은 열에 있는거 제외 하니 24개
# 대각선 chk 가 관건임
'''
  1차원 배열은 결국 x 값이 들어 있는 것이고
  각 열은 y 값 (다음 칸) .. 이렇게 이해 할 것
  
'''


