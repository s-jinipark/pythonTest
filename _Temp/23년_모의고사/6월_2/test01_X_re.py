def solution(n):
    count = 0
    i = 333

    while True:
        k = i
        print(k)
        while k != 0:
            '''
            여기 그냥 숫자 333 이 올 줄은 생각도 못함
            '''
            if k % 1000 == 333 :  #@ @ @ @ @:
                count += 1
                break
            else:
                k = k // 10

        if count == n :  #@ @ @ @ @:
            return i

        i += 1


#n = 1
n = 3

an = solution(n)
print(an)