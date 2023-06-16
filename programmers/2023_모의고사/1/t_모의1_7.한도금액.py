import math

def solution(cards, money):
    cards.sort()
    low = 0
    mid = None
    high = cards[len(cards) - 1]
    print(high)  # 가장 큰
    while low <= high:
        mid = (low + high) // 2
        excess = 0
        for k in cards:
            if k > mid:
                excess += k - mid
        if excess >= money:
            high = mid - 1
        else:
            low = mid + 1
    return (high // 100) * 100

cards = [10000, 8000, 9000, 12000, 7000]
money =5000
ans = solution(cards, money)
print(ans)

'''
1.이번 달에 줄이고 싶은 지출 금액 money를 정합니다.
2.다음과 같이 이번 달 카드 한도를 새로 정합니다.
  2-1. 각 카드별로 지난달 카드 사용 금액과 새 한도 금액을 비교합니다.
  2-2. 지난달 카드 사용 금액이 새 한도 금액보다 큰 경우 (지난달 카드 사용 금액 - 새 한도 금액) 을 모두 더합니다.
  2-3. 위에서 모두 더한 값이 money보다 커야합니다.
3.이번달 사용 금액은 각 카드별로 다음과 같이 사용할 것으로 가정합니다.
  3-1. 지난달에 한도를 초과한 카드는 한도 금액까지만 사용
  3-2. 지난달에 한도를 초과하지 않은 카드는 지난달과 동일한 금액을 사용
4. 단, 한도 금액은 100원 단위로 설정합니다.


'''