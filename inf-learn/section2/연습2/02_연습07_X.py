
##### 소수(에라토스테네스 체)
def chk_prime(x):
    if x < 4:
        return True
    for i in range(2,x): # 1과 자기 자신 빼
        if x % i ==0 :
            return False
    else:
        return True

def solution(N):
    answer = 0
    # 소수가 나오면 그 배수는 모두 체크 해준다는...
    # chk = [True] * (N + 1)
    # for i in range(2, N+1):  # 2 부터 가자..
    #     if chk == False :
    #         continue
    #     print(i, chk_prime(i))
    #     if chk_prime(i)  : # 이게 소수다..그러면
    #         for j in range(i, N, i*2):
    #             print(j)
    #             chk[j] = False
    # print(chk)
    # for k in range(2, N):
    #     if chk[k]:
    #         answer += 1

    cnt = 0
    ch = [0] * (N+1)
    for i in range(2, N+1):
        if ch[i] == 0:
            cnt += 1  # 하 .. 여기서 세준다.
            for j in range(i, N+1, i):  # 마지막이 N+1 이라는 점과 step 이 i 라는 점
                ch[j] = 1
    answer = cnt
    return answer

'''
ch 를 만든다.. index 는 N 까지 나오도록 
그리고 처음 0 으로 셋팅

대충 다 했는데.. 마무리가 잘 안 됬네.
 
'''

N = 20
re = solution(N)
print(re)
#=> 8

N = 90000
re = solution(N)
print(re)
#=> 8713  [그냥 하면, 값은 맞지만, 넘 오래 걸림]

