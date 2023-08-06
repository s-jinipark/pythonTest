
def solution(watch):
    answer = 0
    q = []
    day = 1

    for i in range(0, len(watch)):
        #while day > 3: # org
        #while len(q) > 0 and day > 3:   # 답이 5 로 나옴
        while len(q) != 0 and day -q[0] >3 :  # 문제 이해를 못 함
            q.pop(0)
            answer += 1
        if watch[i] == 1:  #동영상을 담는 행동이 1, 동영상을 시청하는 행동이 0으로 표현됩니다.
            q.append(day)
        elif  len(q) != 0 and watch[i] == 0:
            q.pop(0)
        day += 1
    answer += len(q)
    return answer


watch = [1, 1, 1, 1, 1, 0, 0]
an = solution(watch)
print(an)