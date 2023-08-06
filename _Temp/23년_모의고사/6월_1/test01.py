
def solution(meeting):
    answer = []

    time = [0] * 24

    for i in range(len(meeting)):
        for j in range(len(meeting[i])):
            time [ meeting[i][j] -1] += 1
    print(time)

    max_time = 0
    for i in range(1, 24):
        if time[i] > max_time:
            max_time = time[i]

    for i in range(1, 24):
        if time[i] == max_time:
            answer.append(i +1)

    return answer

meeting = [[8,9,10],[8,10,15],[13]]

an = solution(meeting)
print(an)