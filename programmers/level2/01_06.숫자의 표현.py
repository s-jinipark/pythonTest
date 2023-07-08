def solution(n):
    answer = 0

    # for i in range(1, n+1): # n 까지 돌려면 n+1
    #     연습 = 0
    #     for j in range(i, n+1):
    #         연습 += j
    #         if 연습 == n :
    #             answer +=1
    #             break
    # 효율성에서 걸려서 -> i 가 1/2 을 넘어서면 연속해서 더할 경우 n 을 당연히 넘는다
    # 그럼 n 값 하나만 있을 경우 따로 계산 해 주어야
    for i in range(1, int(n/2)+1):  # +1 까지 해주어야 함
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp == n :
                answer +=1
                break
            elif tmp > n :   # ** 계속 안되서 다시보니 합이 커질 경우 스톱이 없었음..
                break
    answer += 1 # 자신의 수 계산
    return answer

n = 15

re = solution(n)
print(re)
