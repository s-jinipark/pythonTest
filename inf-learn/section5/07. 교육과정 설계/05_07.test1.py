
# 프로그래머스 스타일 로 ...
def solution(pil, N, inp):
    answer = 0

    # find 하면 될거 같은데...
    ans = []
    for i in inp :
        tmp = []
        print(i)
        for ii in i :
            #print(ii)
            #if ii in pil :
            if ii in pil and ii not in tmp:
                tmp.append(ii)
        print(tmp)
        tmp_s = ''
        for j in tmp:
            tmp_s += j
        if tmp_s == pil :
            ans.append('YES')
        else :
            ans.append('NO')
    print(ans)
    return answer

pil = 'CBA'
N = 3
inp = ['CBDAGE', 'FGCDAB', 'CTSBDEA']

re = solution(pil, N, inp)
print('re :', re)
#=>
print('==============================')

pil = 'AFC'
N = 1
inp = ['AFFDCCFF']

re = solution(pil, N, inp)
print('re :', re)
#=>
print('==============================')