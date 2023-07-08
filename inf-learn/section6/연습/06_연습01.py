
##### 재귀함수를 이용한 이진수 출력

# 이름 걍 DFS 로 통일
def DFS(x):
    global rtn
    if x == 0:  # 종료 조건
        return
        #return rtn   # 여기는 걍 return 으로 ...
    else :
        print(x, x%2, x//2)
        rtn = str(x % 2) + rtn  # 순서는 DFS() 호출 전 이냐 후 냐 에 따라...
        x = x//2
        DFS(x)
        # 거꾸로 출력하려면 위 rtn = ... 을 여기에
        print(rtn)

def solution():
    answer = 0
    '''
    이진수 출력 
    단, 재귀함수 이용
    
    1st
    기억이 안 나다
    가까스로 기억해서 풀었는데,
    return 이 잘 안 됨
    '''
    DFS(N)
    print('rtn', rtn)

    return answer

N = 11
rtn = ''
re = solution()
print(re)
#=>
print('====================')

