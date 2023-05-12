def solution(price, money, count):
    answer = -1
    sum = 0
    for i in range(1,count+1):
        print(i)
        sum += price * i

    if sum > money :
        answer = sum - money
    else:
        answer = 0
    return answer


price = 3
money = 20
count = 4
re = solution(price, money, count)
print(re)

'''
[기존]

'''
