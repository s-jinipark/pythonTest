
# 증가수열 만들기(그리디)

def solution():
    answer = 0
    '''
    왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열 을 만듬
    lt, rt 해서...
    
    '''
    cnt = 0
    lt = 0
    rt = N-1
    tmp = []

    while cnt < 5:
        #  적은 값을 가져온다
        if len(tmp) == 0:
            print(inp[lt] , inp[rt])
            if inp[lt] > inp[rt]:
                tmp.append(inp[rt])
                rt -= 1
            else:
                tmp.append(inp[lt])
                lt += 1
        else : # tmp 에 값이 있는 경우
            print(inp[lt] , inp[rt])
            if inp[lt] > inp[rt] and tmp[-1] < inp[rt]:
                tmp.append(inp[rt])
                rt -= 1
            elif inp[lt] <= inp[rt] and tmp[-1] < inp[lt]:
                tmp.append(inp[lt])
                lt += 1

        cnt +=1
    print(tmp)
    return answer


N= 5

inp = [2, 4, 5, 1, 3]

re = solution()
print('re :', re)
#=>
print('==============================')

