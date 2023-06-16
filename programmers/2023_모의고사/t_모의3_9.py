def solution(time):
    answer = 0

    start = "03:00 am"
    end = "06:30 am"

    for t in time:
        if 'pm' in t:
            continue
        print(t)
        time = int(t[:2])
        min = int(t[3:5])
        print(time, min)
        if (time == 6 and min <= 30 ) or (3<= time <= 5):
            answer += 1

    return answer


time = ["06:30 am", "07:00 am", "04:50 am"]   # 기상 시간

ans= solution(time)

print('ans:', ans)