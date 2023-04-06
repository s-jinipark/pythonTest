
import sys
sys.stdin = open("input7-4.txt", "rt")

N = 14
cmd_list =[]
cmd_stack =[]

for i in range(N):
    #print(input())
    tmp_lst = list(input().split())
    #print(tmp_lst)
    cmd_list.append(tmp_lst)

print(cmd_list)

# 굳이 넣었다가 할 필요 있나 싶기도 한데.. 흠..
for l in cmd_list:
    if l[0] == 'push':
        #print('push')
        cmd_stack.append(int(l[1]))
    elif l[0] == 'top':
        if len(cmd_stack) > 0 :
            print(cmd_stack[-1])
        else :
            print(-1)
    elif l[0] == 'size':
        print(len(cmd_stack))
    elif l[0] == 'empty':
        if len(cmd_stack) > 0 :
            print(0)
        else :
            print(1)
    elif l[0] == 'pop':
        if len(cmd_stack) > 0 :
            tmp = cmd_stack.pop()
            print(tmp)
        else :
            print(-1)

#print(cmd_stack)

print('-------------------------')

#inp1 = '()(((()())(())()))(())'
inp1 = '(((()(()()))(())()))(()())'

i_stack = []
cnt = 0

for i in inp1:
    #print(i)
    if i == '(' :
        i_stack.append(i)
    elif i == ')' :
        # 일단 빼
        tmp = i_stack.pop()
        cnt += len(i_stack)
print(cnt)
# 두번 째 inp 은 값이 다르게 나옴
'''
레이저가 나와서 잘리는 경우와
쇠막대기가 끝나는 부분을 구분해야 함

바로 앞을 참조해야 함
'''

print('-------------------------')

# 초기화
i_stack = []
cnt = 0
for i in range(len(inp1)):
    #print(inp1[i])
    if inp1[i] == '(':
        i_stack.append(inp1[i])
    else:
        if inp1[i-1] == '(':  # 레이저 네...
            i_stack.pop()
            cnt += len(i_stack)
        else:
            i_stack.pop()
            cnt += 1
print(cnt)

print('-------------------------')

#inp1 = '4 2'
#inp2 = '1924'
#inp1 = '7 3'
#inp2 = '1231234'
inp1 = '10 4'
inp2 = '4177252841'
cnt = 0

N, K = map(int, inp1.split())

in_stack = [inp2[0]]   # 맨 앞 값을 넣는다

for i in range(1,N):
    #print(in_stack[-1], inp2[i])
    if in_stack[-1] < inp2[i] and cnt < K:
        in_stack.pop()
        cnt += 1
    in_stack.append(inp2[i])

print(in_stack)

# 웁스 마지막거에서 걸림...
# 뺄 수 있을 때 까지 계속 작은 수 뺀다

# 다시 해봄
in_stack = [inp2[0]]   # 맨 앞 값을 넣는다

for i in range(1, N):
    while in_stack[-1] < inp2[i] and cnt < K :
        #print(in_stack[-1], in_stack)
        #in_stack.pop()
        del(in_stack[-1])
        cnt += 1
    in_stack.append(inp2[i])

print(in_stack)

# 이상하게 루핑을 안 도는 거 같음

# int 로 바꿔서 다시 해봄
n2, k2 = map(int, inp1.split())
lst2 = []
cnt2 = 0

for c in inp2:
    lst2.append(int(c))

print(n2, k2, lst2)
stk2 = []
for i in range(n2):
    while stk2 and stk2[-1] < lst2[i] and cnt2 < k2:
        print(lst2[i])
        stk2.pop()
        cnt2 += 1
    stk2.append(lst2[i])

print(stk2)