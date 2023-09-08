
# 쇠막대기
def solution():
    answer = 0
    '''
    풀었던 기억과 그림을 보면
    ')' 가 왔을 때 
      '(' 가 stack 에  있으면, 맨위 빼주고, 남아있는 갯수를 세준다
      
    '(' 는 그냥 넣어 줌
    
    그런데.
      바로 앞의 기호를 기억해야(?) 할 듯... 
      그래야..레이저 인지.. 쇠막대기의 끝인지 구분이 됨
      
    풀이 봤더니
      stack 과 원래 str 에서 직전 값을 참조해서 푼다
    '''

    stack = []
    sum = 0
    for i in range(len(inp)):
        #print(i, inp[i])
        if inp[i] == '(':
            stack.append(inp[i])
        elif inp[i] == ')':
            if inp[i-1] == '(' : # i-1 은 있기 마련
                stack.pop()  # 레이저 인 경우
                sum += len(stack)
            else : # 그 외 는 쇠막데기 인 경우
                stack.pop()
                sum += 1
    print(sum)
    return answer


inp = '()(((()())(())()))(())'

re = solution()
print('re :', re)
#=> 17
print('==============================')

inp = '(((()(()()))(())()))(()())'

re = solution()
print('re :', re)
#=> 24