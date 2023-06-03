
def DFS(x, chk, flag):
    #print(N, inp, chk)
    print('f:', flag)
    if x == N :
        #print(inp)
        grp0 = 0
        grp1 = 0
        for i in range(N):
            if chk[i] == 0 :
                grp0 += inp[i]
            else :
                grp1 += inp[i]
        print(grp0, ' : ', grp1)
        if grp0 == grp1 :
            flag = 'YES'
            print('*****')
            return
        return
    else :
        chk[x] = 0
        DFS(x+1, chk, flag)
        chk[x] = 1
        DFS(x+1, chk, flag)


def solution(N, inp):
    answer = '' #0

    chk = [0] * N
    print(chk)
    flag = 'NO'
    DFS(0,  chk, flag)
    print('>', flag)
    return answer

N = 6
inp = [1,3,5,6,7,10]
flag = ''
re = solution(N, inp)
print('re :', re)
#=>
print('==============================')
