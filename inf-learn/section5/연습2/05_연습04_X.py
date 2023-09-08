
##### 후위식 연산
def solution():
    answer = 0

    stack = []
    for x in inp:
        print(x)

        if x.isdecimal() :
            stack.append(int(x))
        else:
            if x == '+' :
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2+n1)  # 순서도 맞춰준다
            elif x == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif x == '*' :
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 * n1)
            elif x == '/' :
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 / n1)
    print(stack)
    return answer

'''
t1, t2 순서를 잘해야...
여기는 stack 에 숫자를 넣는다는 

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
