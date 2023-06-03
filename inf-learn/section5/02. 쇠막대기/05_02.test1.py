
# 프로그래머스 스타일 로 ...
def solution(inp):
    answer = 0
    stk = []

    # for i in inp:
    #     #print(i)
    #     if (i == '('):
    #         stk.append(i)
    #     elif (i == ')'):
    #         if stk[-1] == '(':
    #             stk.pop()
    #             # stk 에 남아 있는 갯수
    #             answer += len(stk)
    #     print(stk, 'len: ', len(stk) , answer)

    # 값이 다름
    # 닫는 괄호 일 때 무조건 stack 갯수를 세면 안됨
    # 막대기의 끝인지, 레이저의 끝인지를 구별해야 함
    prev = ''
    for i in inp :
        if (i == '('):
            stk.append(i)
        elif (i == ')'):
            # 바로 전 거랑 비교해서.
            if prev == '' : # 처음이면 레이저
                stk.pop()
            else:
                if prev == '(' : # 레이저의 끝
                    stk.pop()
                    answer += len(stk)
                elif prev == ')' : # 쇠막대기의 끝
                    stk.pop()
                    answer += 1
        prev = i

    return answer


inp = '()(((()())(())()))(())'

re = solution(inp)
print('re :', re)
#=>
print('==============================')


inp = '(((()(()()))(())()))(()())'

re = solution(inp)
print('re :', re)
#=>
print('==============================')