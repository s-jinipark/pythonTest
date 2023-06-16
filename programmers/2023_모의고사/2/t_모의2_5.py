def solution(num):
    while (num >= 10):
        total = 0
        while num > 10:
            total += num % 10
            num = num // 10
        #num = total
        num = total
    return num

num= 345

ans= solution(num)
print('ans:', ans)


num= 1234

ans= solution(num)
print('ans:', ans)

