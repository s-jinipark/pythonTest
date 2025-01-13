def solution(n):
    answer = 0

    # 큰 단위의 화폐부터 차례대로 확인
    coin_types = [500, 100, 50, 10]

    for coin in coin_types :
        #print(coin)
        print(n//coin)  # 몫을 구하는 거
        answer += n//coin
        print(n%coin)  # 나머지를 구하는 거
        n = n%coin
    return answer


n = 1260
print("----- -----")
print(solution(n))