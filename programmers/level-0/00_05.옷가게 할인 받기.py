def solution(price):
    answer = 0

    if price >= 500000:
        #answer = price - int(price * 0.2)
        answer = int(price * 0.8)
    elif price >= 300000:
        #answer = price - int(price * 0.1)
        answer = int(price * 0.9)
    elif price >= 100000:
        #answer = price - int(price * 0.05)
        answer = int(price * 0.95)
    else :
        answer = price
    return answer

#p = 150000
p = 580000
re = solution(p)

print(re)
print("====================")

