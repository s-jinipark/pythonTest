
# 352*72-/+ 가 나와야 되는데 352*72-/*+ 가 나옴
# 풀이를 보고 ...
# def solution(inp):
#     answer = 0
#     stk = []
#     res = ''
#     for x in inp:
#         print(x, x.isdecimal())  # **
#
#         if x.isdecimal() :
#             res += x
#         else :
#             if x=='(':
#                 stk.append(x)
#             elif (x == '*' or x == '/') :
#                 while stk and (stk[-1] == '*' or stk[-1] == '/') :
#                     res += stk.pop()
#                 stk.append(x)  # 우선 순위가 같은 경우 stk 에 있던거 먼저 처리하고 x(자신)를 넣는다
#             elif (x == '+' or x == '-') :
#                 while stk and stk[-1] != '('  :
#                     res += stk.pop()
#                 stk.append(x)
#             elif x == ')' :
#                 while stk and stk[-1] != '('  :
#                     res += stk.pop()
#                 stk.pop()  #  '(' 까지 빼준다
#     while stk:  # 나머지 친구들
#         res += stk.pop()
#
#     print('res : ', res)
#     return answer

# 프로그래머스 스타일 로 ...
def solution(inp):
    answer = 0
    stk = []
    tmp = ''

    for i in inp:
        #print(i)

        if i in '*/':
            # # 낮은 연산자 빼고 // 넣는다
            # 가 .. 아니고, 우선 순위 높으면 스택에 담는다
            for j in range(len(stk)-1, -1, -1):

                if stk[j] in '*/' :
                    #연습 += stk[j]
                    # 빼는 걸로  (*** 마지막에 고쳤음) , 이거 : 352*72-/+ 가 나와야 되는데 352*72-/*+ 가 나옴)
                    tmp += stk.pop()
                stk.append(i)

        elif i in '+-':
            stk.append(i)
        elif i == '(':
            stk.append(i)
        elif i == ')':
            # ( 까지 pop 한다
            for j in range(len(stk)-1, -1, -1):
                tmp_in = stk.pop()
                if tmp_in == '(':
                    break
                else :
                    tmp += tmp_in

            stk.pop()
        else :
            tmp += i
        print(tmp)

    # 만약 스택에 남아 있다면
    while len(stk) > 0 :
        tmp += stk.pop()

    print('>' , tmp)
    return answer


inp = '3+5*2/(7-2)'

re = solution(inp)
print('re :', re)
#=>
print('==============================')

