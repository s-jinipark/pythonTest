
##### 소수(에라토스테네스 체)
def prime_yn(x):
    rtn = True
    for i in range(2, x):
        if x%i == 0 :
            rtn = False
    return  rtn

def solution(N):
    answer = 0

    # 그냥 하면..
    for i in range(2, N+1):  # 1 부터 하면 ?? 갯수 하나 증가 ...
        #print(i)
        if prime_yn(i)  :
            print(i)
            answer += 1
    return answer

N = 20
re = solution(N)
print(re)
#=> 8

N = 90000
re = solution(N)
print(re)
#=> 8713  [그냥 하면, 값은 맞지만, 넘 오래 걸림]

