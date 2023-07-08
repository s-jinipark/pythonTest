
##### 후위식 연산
def solution():
    answer = 0

    stack = []
    sum = 0
    for i in inp:
        print(i)
        if i.isdecimal() :
            stack.append(i)
        else:
            # stack 에 2개 있다는 얘기 아님?
            t2 = int(stack.pop())
            t1 = int(stack.pop())
            tmp = 0
            if i == '+':
                tmp = t1 + t2
            elif i == '-':
                tmp = t1 - t2
            elif i == '*':
                tmp = t1 * t2
            elif i == '/':
                tmp = t1 / t2
            stack.append(str(tmp))
    print(stack)
    return answer

'''
t1, t2 순서를 잘해야...

'''

inp = '352+*9-'
re = solution()
print(re)
#=> 12
print('====================')

inp = '573*+5-323*++'
re = solution()
print(re)
#=> 30
