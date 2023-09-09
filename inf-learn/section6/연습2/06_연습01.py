
##### 재귀함수를 이용한 이진수 출력

# 이름 걍 DFS 로 통일

def DFS(x):
    if x == 0:
        return
    global rtn
    rtn = str(x % 2) + rtn
    print(x//2, x % 2)
    x = x//2   # 11 -> 5 -> 2 -> 1
    DFS(x)

def solution():
    answer = 0

    DFS(N)
    print(rtn)
    return answer

N = 11
rtn = ''
re = solution()
print(re)
#=>
print('====================')

