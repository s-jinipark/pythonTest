def solution(n):
    answer = 0

    # 이진수 변환
    print(bin(n))
    tmp = bin(n)
    print(type(tmp))
    tmp = tmp.replace('0b', '')
    n_1 = 0
    for i in tmp:
        print(i)
        if i == '1':
            n_1 += 1
    print('>', n_1)

    while True:
        n_2 = 0
        n += 1
        tmp = bin(n)
        tmp = tmp.replace('0b', '')
        for i in tmp:
            #print(i)
            if i == '1':
                n_2 += 1
        if  n_1 == n_2  :
            break
    answer = n
    return answer


n = 78
re = solution(n)
print(re)

n2 = 15
re2 = solution(n2)
print(re2)

