def solution(num):
    while (num >= 10):
        total = 0
        #while num > 10:
        while num > 0:   # [2] 아.. print 가 다르게 찍힘, [제출하기] 에서 통과 됨
            total += num % 10
            num = num // 10
            print(total, num)
        #num = total   # 맨 첨
        #total += num  # 이걸루 하면 [코드 실행까지는 맞음]
        num = total  # 다시 이거루...

    return num

num= 345

ans= solution(num)
print('ans:', ans)


num= 1234

ans= solution(num)
print('ans:', ans)

'''
이거 함정 죽임..
'''