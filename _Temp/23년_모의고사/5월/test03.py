
# 스택 구현하기_빈칸채우기

stack = [0] * 10000
top = -1
answer = 0


def func_a(x):
    global top, stack
    top += 1
    stack[top] = x


def func_b():
    global answer, top
    answer = top +1


def func_c():
    global top, stack
    top -= 1


def solution(command):
    global answer, top, stack
    for c in command:
        if c == "pop":
            #stack.pop()
            func_c()
        else:
            x = int(c[5])
            #stack.append(x)
            func_a(x)
    func_b()
    return answer


'''

'''

command = ["push 3", "push 1", "pop", "push 5"]

an = solution(command)
print(an)