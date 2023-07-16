
##### 알파코드(DFS)

def DFS(L, P):
    if L == n:
        print(res)
        for j in range(P):
            #print(res[j], end=' ')
            print(chr(res[j]+64), end='')
        print()
    else :
        for i in range(1, 27):  # 알파벳 수 대로..
            if inp[L] == i:   # 한자리..
                res[P]= i
                DFS(L+1, P+1)
            elif i>10 and inp[L] == i//10 and inp[L+1] == i%10 :
                # 뒷자리 까지 확인한다는 점
                res[P] = i
                DFS(L+2, P+1)

def solution():
    answer = 0

    '''
    상태 트리
    알파벳 개수 만큼 1~26 개로 뻗는다.
    
    이건 문제 풀어보고, 공식 처럼 암기해야 
    머... 될 듯...
    '''

    DFS(0, 0)
    print('res', res)
    return answer


#inp = '25114'
inp = [2,5,1,1,4]
n = len(inp)
res = [0] * (n+3)

# 이경우 4 로 끝나서 그렇지
# 1 이나 2 로 끝나면 다음자리도 확인해야 해서...
inp.insert(n, -1)

re = solution()
print(re)
#=>
print('====================')
