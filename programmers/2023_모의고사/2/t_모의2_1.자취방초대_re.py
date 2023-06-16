def solution(schedule):
    answer = 0
    for i in range (len(schedule)):
        if  schedule[i][0] >5 :   # 친밀도 5 보다 큰 경우
            schedule[i][2] += 5
    print(schedule)

    for i in range(len(schedule) - 1, 0, -1):
        for j in range(0, i):
            print(i, j)   # 정렬
            if  schedule[j][2] > schedule[j + 1][2]:
                temp = schedule[j]
                schedule[j] = schedule[j + 1]
                schedule[j + 1] = temp
    print(schedule)
    # 끝나는 시간으로 sort

    t = 0
    for i in range (len(schedule)):
        if t <= schedule[i][1]:
            answer += 1
            t = schedule[i][2]

    return answer

# 친밀도, 방문 시작 시각, 방문 종료 시각]
schedule = [[7,5,10], [2,10,15], [5,15,40], [10,40,70]]


ans= solution(schedule)

print('ans:', ans)

'''
1st -> 20 점 밖에 안 나옴

'''