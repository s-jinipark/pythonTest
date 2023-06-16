def solution(dates):
    answer = 0

    for i in range(len(dates)):
        print(dates[i].replace('/',''))
        dates[i] = dates[i].replace('/', '')

    sample = '1248'

    for i in dates:
        tmp = 0
        for j in i :
            print(j)
            if j in sample:
                tmp += 1
        if tmp == len(i):
            answer += 1
    return answer

dates = ["2/14", "6/8", "10/13"]

ans= solution(dates)
print('ans:', ans)
