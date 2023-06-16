def solution(schedule):
    answer = 0
    print(schedule)
    for i in range (len(schedule)):
        if schedule[i][0] == 5:    #<--
            schedule[i][2] += 5

    print(schedule)

    for i in range(len(schedule) - 1, 0, -1):
        for j in range(0, i):
            print(i, j)
            if schedule[i][2] < schedule[j][2]:    # 종료 시간
                temp = schedule[j]
                schedule[j] = schedule[j + 1]
                schedule[j + 1] = temp
    print(schedule)
    t = 0
    for i in range (len(schedule)):
        if t <= schedule[i][1]:
            answer += 1
            t = schedule[i][2]

    return answer


schedule = [[7,5,10], [2,10,15], [5,15,40], [10,40,70]]


ans= solution(schedule)

print('ans:', ans)