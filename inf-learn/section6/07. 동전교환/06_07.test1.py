

def solution(coin, M):
    answer = 0

    # 보통은 큰 동전 순서로 계산.
    coin.sort(reverse=True)
    print(coin)
    for c in coin:
        print(M, c, M//c, M % c, answer)
        if M <c :
            continue
        answer += M // c
        if M % c == 0:
            break
        else :
            M = M % c

    return answer

N = 3   # 동전의 종류
coin = [1,2,5]   # 동전 종류
M = 15  # 거슬러 줄 금액

re = solution(coin, M)

print('re :', re)
#=>
print('==============================')


N = 5   # 동전의 종류
coin = [1,5,7,11,15]   # 동전 종류
M = 39  # 거슬러 줄 금액

re = solution(coin, M)

print('re :', re)
#=> 5
print('==============================')


N = 5   # 동전의 종류
coin = [1,8,20,25,50]   # 동전 종류
M = 129  # 거슬러 줄 금액

re = solution(coin, M)

print('re :', re)
#=> 여기서 좀 달라짐. 난 7 답 5
'''
    [   50, 25, 20, 8, 1]
나   :  2   1           4
강의 :  2        1   1   1
'''
print('==============================')