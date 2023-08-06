
def solution(price):
    answer = 0
    pre = price[0]
    for i in range(1, len(price)) :
        print(price[i])
        if pre < price[i]:
            answer += 20
        elif pre > price[i]:
            answer -= 15
        pre = price[i]
    return answer

price = [1000, 1200, 900, 700, 1000, 1100]

re = solution(price)
print(re)