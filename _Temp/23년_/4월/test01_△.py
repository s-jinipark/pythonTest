
# 자취방 초대

def solution(schedule):
    answer = 0
    for i in range (len(schedule)):
        if schedule[i][0] > 5 :  # 친밀도가 5보다 큰 손님이 ->  5분 plus
            schedule[i][2] += 5

    for i in range(len(schedule) - 1, 0, -1):
        for j in range(0, i):
            print(i , j)
            if  schedule[j][2] > schedule[j + 1][2] :  # 종료시간 기준 정렬
                temp = schedule[j]
                schedule[j] = schedule[j + 1]
                schedule[j + 1] = temp


    t = 0
    for i in range (len(schedule)):
        if t <= schedule[i][1]:
            answer += 1
            t = schedule[i][2]
    print(schedule)

    return answer


'''
끝나는 시간으로 정렬해서...
맞춰 나가는데, 친밀도가 있어서, 
-> 친밀도가 5보다 큰 손님이 방문을 마친 후에는 휴식을 위해 5분 동안 다른 손님을 맞이하지 않기로 했습니다.
[피곤함 반영..인 듯]

'''

# [친밀도, 방문 시작 시각, 방문 종료 시각]
schedule = [[7, 5, 10], [2, 10, 15], [5, 15, 40], [10, 40, 70]]

an = solution(schedule)
print(an)