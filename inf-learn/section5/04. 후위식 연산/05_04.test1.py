
# 프로그래머스 스타일 로 ...
def solution(inp):
    answer = 0

    # 스택으로 해야 됨
    stk = []
    for i in inp:
        print(i)
        # 연산자가 나왔다는 것은 숫자 2개가 stk 에 있다는 말
        if i in '+-*/' :
            end =stk.pop()
            frt =stk.pop()
            c = 0
            if i == '+':
                c = frt + end
            elif i == '-':
                c = frt - end
            elif i == '*':
                c = frt * end
            elif i == '/':
                c = frt / end
            # 그리고 계산된 값은 넣어 주어야
            stk.append(c)
        else :
            stk.append(int(i))
    print(stk)
    answer = stk[0]  # 값이 하나만 있을 테니...

    ########## second
    # 연습 = inp
    # while len(연습) > 0:
    #     c = 0
    #     front = ''
    #     end = ''
    #     for i in range(len(연습)):
    #         # 연산자가 나오면 앞 두자리 계산하고 끝냄
    #         if 연습[i] == '+' :
    #             c = int(연습[i-2]) + int(연습[i-1])
    #         elif 연습[i] == '-' :
    #             c = int(연습[i-2]) - int(연습[i-1])
    #         elif 연습[i] == '*' :
    #             c = int(연습[i-2]) * int(연습[i-1])
    #         elif 연습[i] == '/' :
    #             c = int(연습[i-2]) / int(연습[i-1])
    #
    #         if c != 0 :  # 값이 들어 왔어.. 그렇다면
    #             print(i,  연습[i - 2], 연습[i - 1], 연습[:i - 2], 연습[i+1:])
    #             front = 연습[:i - 2]
    #             end = 연습[i+1:]
    #             break
    #
    #     연습 = front + str(c) + end
    #
    #     print(연습)

    ########## first
    # for i in inp):
    #     print(i)
    #     if i in '+-*/':
    #         # 연산자가 나왔으니, 앞에 2자리가 있다고 가정할 수 있다
    #         print(i, inp[:i], inp[i-2], inp[i-1], inp[:i-2])

        # if inp[i] == '+' :
        #     연습 = int(inp[i-2]) + int(inp[i-1])
        #
        # elif inp[i] == '-' :
        #     연습 = int(inp[i-2]) - int(inp[i-1])
        # elif inp[i] == '*' :
        #     연습 = int(inp[i-2]) * int(inp[i-1])
        # elif inp[i] == '/' :
        #     연습 = int(inp[i-2]) / int(inp[i-1])

    return answer

inp = '352+*9-'

re = solution(inp)
print('re :', re)
#=> 12
print('==============================')

inp = '573*+5-323*++'

re = solution(inp)
print('re :', re)
#=> 30
print('==============================')

