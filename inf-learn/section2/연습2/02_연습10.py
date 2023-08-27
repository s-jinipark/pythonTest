
##### 점수 계산
def solution(N):
    answer = 0
    tot = [0] * N   # 점수를 넣을 수 있게
    for i in range(N):
        if inp[i] == 1:
            if i == 0 :
                tot[i]= 1
            else:
                tot[i] = tot[i-1] +1
    print(tot)
    answer = sum(tot)
    return answer


N = 10
inp = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]

re = solution(N)
print(re)
#=> 10


N = 30
inp = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

re = solution(N)
print(re)
#=> 465
