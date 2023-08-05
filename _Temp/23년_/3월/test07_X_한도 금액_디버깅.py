
import math

def solution(cards, money):
    cards.sort()
    low = 0
    mid = None
    high = cards[len(cards) - 1]
    #high = len(cards) - 1   # 이건 아닌 듯
    while low <= high:
        mid = (low + high) // 2
        excess = 0
        for k in cards:
            if k > mid:
                excess += k - mid
        #if excess >= money:
        if excess < money:   # 하.. 시도는 했었는데...
            high = mid - 1
        else:
            low = mid + 1
    return (high // 100) * 100


cards = [10000, 8000, 9000, 12000, 7000]
money = 5000

an = solution(cards, money)
print(an)