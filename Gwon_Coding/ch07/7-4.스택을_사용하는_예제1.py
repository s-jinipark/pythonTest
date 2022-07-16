

# 스택을 통해서 사용하는 기능은 5 가지
# 1. push : 데이터를 스택에 추가한다 (append)
# 2. pop : 스택의 최상단 데이터를 삭제한다
# 3. top : 스택의 최상단 데이터가 무엇인지 확인한다
# 4. size : 스택에 데이터가 몇 개 들어 있는지 확인한다
# 5. empty : 스택이 비어 있는지 확인한다

# 7-4 스택을 사용하는 예제 1

import sys

sys.stdin = open("input7-4.txt", "rt")
n = int(input())  # N 명

# 7-5 스택을 사용하는 예제 2
# 쇠막대기 문제
# 여러 개의 쇠막대기를 레이저로 절단
#  . 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다 (끝점은 겹치지 않도록)
#  . 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다
#  . 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다
# 예제 입력                      출력
#   ()((()())(())()))(())       17

'''
붙어 있는 괄호 () : 레이저를 발사하여 현재 위치에서 쇠막대기를 자른다
붙어 있지 않는 괄호 ( : 쇠막대기가 새로 생성되는 위치이다
붙어 있지 않는 괄호 ) : 쇠막대기가 종료되는 위치이다

(((()()))) 를 예시로 본다면
'(((' 쇠막대기 3개 생성
'()' 레이저를 발사하면 쇠막대기의 총 개수는 3이 추가
'()' 레이저를 발사하면 쇠막대기의 총 개수는 3이 추가
')' 쇠막대기가 종료될 때 총 개수 1 추가
')' 쇠막대기가 종료될 때 총 개수 1 추가
')' 쇠막대기가 종료될 때 총 개수 1 추가
'''

inp = "()(((()())(())()))(())"
#tmp_list = list(inp.split())  # ?? 이거 안됨 ['()((()())(())()))(())']
tmp_list = []
for i in inp:
    tmp_list.append(i)
print(tmp_list)

tmp_stack = []
sum =0
# for c in tmp_list :
#     if c == '(' :
#         tmp_stack.append(c)
#     if c == ')' :
#         print(tmp_stack[-1])
#         print(len(tmp_stack))
#         # 레이저인걸 어떻게 식별??
#         # => 주어진 문자열 확인해서.. ㅠ

# [2] 번째 - 인덱스를 사용해야 해서 range 로
for i in range(len(tmp_list)) :
    if tmp_list[i] == '(' :
        tmp_stack.append(tmp_list[i])
    if tmp_list[i] == ')' :
        if tmp_list[i-1] == '(' : # 레이저 구분
            tmp_stack.pop()
            sum += len(tmp_stack)
            #print(sum)
            #print(tmp_stack)
        else :
            tmp_stack.pop()
            sum += 1
print(sum)

# 7-6 스택을 사용하는 예제 3
# 크게 만들기
# N 자리 숫자가 주어졌을 때, 여기서 숫자 K 개를 지워서 얻을 수 있는 가장 클 수를 구하는 프로그램 작성

# 예제 입력 4 2         출력
#          1924        94
# 예제 입력 7 3         출력
#          1231234     3234
# 예제 입력 10 4        출력
#          4177252841  775841

print("--------------------")

inp = '1924'
n = 4
k = 2   # 지울 수 있는 수
tmp_stack2 = []
ans2 = ''
for i in range(n):
    print(inp[i])
    if len(tmp_stack2) == 0 :  # 처음엔 append
        tmp_stack2.append(inp[i])
    else :
        print(tmp_stack2[-1])
        if tmp_stack2[-1] < inp[i] : # 새로 온 수가 크다
            tmp_stack2.append(inp[i]) # 차곡차고 쌓아

        else :  # 새로 온 수가 작어
            ans2 += tmp_stack2.pop()
            tmp_stack2.append(inp[i])
print('>', ans2)

# 계속 큰 수가 오면 스택에 쌓고
# 단순하게 스택 상단 보다 크고, 다음 오는 수보다 크면 선택했는데
# 그 외 (계속 더 큰 수만 올때의 처리...) 잘 모름

