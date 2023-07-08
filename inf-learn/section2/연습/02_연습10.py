
##### 점수 계산
def solution(N):
    answer = 0
    chk = [0] * N

    # 첫번째 그냥 넣어
    chk[0] = inp[0]
    for i in range(1,N):
        if inp[i] == 1 :
            chk[i] = chk[i-1] + 1

    print(chk, sum(chk))

    return answer


N = 10
inp = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]

re = solution(N)
print(re)
#=>



