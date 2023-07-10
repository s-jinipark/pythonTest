
# 가장 큰 수
def solution():
    global  m
    answer = 0
    '''
    m 개를 제거하고, 순서유지, 가장 큰 숫자
    앞에 나보다 작은 수는 제거
    
    스택을 써야 겠다는 OK
    구현이 안 따라 줌.. 
    '''
    stack = []
    s_su = str(su)
    for x in s_su:
        while stack and m > 0 and stack[-1]< x:
            # 웁스 여기다 조건을 다 넣어 줌, 어이가 없다!
            stack.pop()
            m -= 1
        stack.append(x)
    print(stack)
    if m!= 0:
        stack =stack[:-m]
    print(stack)
    return answer


su = 5276823
m = 3   # 제거할 m개 숫자

re = solution()
print('re :', re)
#=> 7823
print('==============================')

su = 9977252641
m = 5   # 제거할 m개 숫자

re = solution()
print('re :', re)
#=> 99776
