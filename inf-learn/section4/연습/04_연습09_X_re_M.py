
# 증가수열 만들기(그리디)

def solution():
    answer = 0
    '''
    설명 듣고 품
    
    '''
    cnt = 0
    lt = 0
    rt = N-1
    last = 0
    tmp = []
    res = ''
    #while cnt < 3:
    while lt <= rt :
        print(cnt)
        if inp[lt] > last:
            tmp.append((inp[lt], 'L'))
        if inp[rt] > last:
            tmp.append((inp[rt], 'R'))
        tmp.sort()
        print(tmp)
        if len(tmp) == 0:
            break
        else :
            res = res + tmp[0][1]
            last = tmp[0][0]
            if tmp[0][1] == 'L':
                lt += 1
            else:
                rt -= 1
        tmp.clear()
        #cnt += 1
    print(len(res))
    print(res)
    return answer


N= 5

inp = [2, 4, 5, 1, 3]

re = solution()
print('re :', re)
#=>
print('==============================')

