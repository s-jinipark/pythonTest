
##### 소수(에라토스테네스 체)

def solution(N):
    answer = 0

    # 풀이 보고 ...
    chk = [0] * (N+1)
    cnt = 0
    for i in range(2, N+1):  # 2 ~ N+1 임.
        #print(i)
        if chk[i] == 0 :
            cnt += 1
            for j in range(i, N+1, i) :
                chk[j] = 1
    print(cnt)
    return answer

'''
글쎄 이건 외우지 않고서야..

'''
N = 20
re = solution(N)
print(re)
#=> 8

N = 90000
re = solution(N)
print(re)
#=> 8713  [그냥 하면, 값은 맞지만, 넘 오래 걸림]

