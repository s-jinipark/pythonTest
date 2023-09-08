
# 후위표기식 만들기
def solution():
    answer = 0
    '''
    이건 뭐 기억이 안남
    
    괄호 먼저 정리하고
    곱하기 -> 더하기.. 이런 순으로 해야 할 듯
    
    풀이보고 해봤는데 사실 이해 안감
    '''
    stack = []
    res = ''
    for i in inp:
        print(i)
        if i.isdecimal() :   # isdecimal() 로 구분
            res += i
        else:
            if i == '(':  # 그냥 골인
                stack.append(i)
            elif i == '*' or i == '/' : # 곱하기 or 나누기
                while stack and (stack[-1] == '*' or stack[-1]=='/') :
                    # 위 while 문을 잘 기억해야 할 듯
                    res += stack.pop()
                stack.append(i)  # 자기는 다시 넣어?
            elif i == '+' or i == '-':
                while stack and (stack[-1] != '('):
                    res += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and (stack[-1] != '('):
                    res += stack.pop()
                stack.pop()
    # 남은 애들
    while stack:
        res += stack.pop()
    print(res)
    return answer


inp = '3+5*2/(7-2)'


re = solution()
print('re :', re)
#=> 352*72-/+
print('==============================')

