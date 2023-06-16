def solution(month, date):
    answer = []
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    cnt = 100
    while cnt > 1:
        #if date + 1 < day[month]:
        if date  < day[month]:
            date += 1
        else:
            date = 1
            month += 1
            if month > 12:
                month = 1
        print(month, date)
        cnt -= 1

    answer.append(month)
    answer.append(date)
    return answer


month = 10
date = 3
ans= solution(month, date)

print('ans:', ans)