def get_cds(n, limit, power):
    cnt = 0
    for i in range(1, int(n**(1/2)) +1) :  # 포인트1. 제곱근 만큼 반복
        if n % i == 0:
            if i == n//i :  # 제곱근일 경우 -> 1개만 카운트
                cnt += 1
            else :
                cnt += 2  # 제곱근이 아닐 경우, 2개 카운트 (i, n//i)
        if cnt > limit :  # 포인트2. 소수의 개수가 limit 을 넘어가면
            return power  # 강제로 power 리턴
    return cnt

def solution(number, limit, power):
    answer = 0

    # s = [0] * (number+1)
    # s[1] =1
    # print(s)

    total = 1

    for i in range(2, number+1) :
        tmp = get_cds(i, limit, power)
        total += tmp

    answer = total

    return answer

number = 10  #5
limit = 3
power = 2

re = solution(number, limit, power)
print(re)

'''
[기존] 시간 초과

def solution(number, limit, power):
    answer = 0

    s = [0] * (number+1)
    s[1] =1
    print(s)

    for i in range(2, number+1) :
        print(i)
        cnt = 0
        for j in range(1, (i+1)):
            if i % j == 0:
                print('>', j)
                cnt += 1
        s[i] = cnt
    print(s)

    # 계산
    for i in range(1, len(s)):
        if s[i] > limit :
            answer += power
        else :
            answer += s[i]

    return answer
'''