
##### 주사위 게임
def solution(N):
    answer = 0
    '''
    규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
    규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
    규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
    '''
    maxVal = 0
    # 3개의 주사위라고 정해 있긴 함
    for i in range(N):
        x,y,z = inp[i]
        print(x,y,z)
        if x==y and y==z and z==x :
            answer = 10000 + (x *1000)
        elif x==y  or y==z :
            answer = 1000 + (y *100)
        elif   z==x :
            answer = 1000 + (z *100)
        else:
            answer = max(inp[i]) *100
        print(answer)
        if maxVal < answer :
            maxVal = answer
    #return answer
    return maxVal

N = 3
inp = [[3,3,6],
       [2,2,2],
       [6,2,5]]
re = solution(N)
print(re)
#=>



