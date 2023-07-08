
##### 교육과정 설계

def solution():
    answer = 0
    '''
    어떻게?
    inp 를 루핑돌면서 필수만 뽑아냄.. 중복되면 한번만 넣고..
    그 다음에 pil (필수) 랑 맞춰봄
    '''

    for i in inp:
        print(i)
        tmp = []
        for j in i:
            #print(j)
            if j in pil:
                #print(j)
                if j not in tmp:
                    tmp.append(j)
        #print(tmp)

        # 필수 랑 비교
        comp = ''
        for k in tmp:
            comp += k
        #print(comp)
        if comp == pil :
            print('YES')
        else :
            print('NO')
        tmp.clear()

    return answer

N = 3
pil = 'CBA'
inp = ['CBDAGE', 'FGCDAB', 'CTSBDEA']

re = solution()
print(re)
#=>
print('====================')

N = 1
pil = 'AFC'
inp = ['AFFDCCFF' ]

re = solution()
print(re)