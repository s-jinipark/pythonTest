
##### 단어 찾기

def solution():
    #answer = 0
    answer = ''
    ''''
    여러 방법이 있겠지만 dict 에 넣어 놓고
    inp 가 왔을 때 -1 하는 ...
    '''

    tmp = dict()
    for p in plan:
        if p not in tmp:
            tmp[p] =1
        else:
            tmp[p] +=1
    print(tmp)

    # 빼냄
    for i in inp:
        if i in tmp:
            tmp[i] -= 1
    print (tmp)

    # 1 인 거 찾는다. [코딩이 별로인거 같아]
    for k in tmp:
        #print(tmp[k])
        if tmp[k] == 1:
            answer = k
            break
    print(k)
    return answer

N = 5
plan = ['big','good','sky','blue','mouse']
inp = ['sky','good','mouse','big']

re = solution()
print(re)
#=>
print('====================')

