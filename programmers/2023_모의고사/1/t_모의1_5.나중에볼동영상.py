def solution(watch):
    answer = 0
    q = []
    day = 1

    for i in range(0, len(watch)):
        while day >= 3 and len(q) != 0 and q[0]==1:
            q.pop(0)
            answer += 1
        if watch[i] == 1:
            q.append(day)
        elif  len(q) != 0 and watch[i] == 0:
            q.pop(0)
        day += 1
    answer += len(q)
    return answer



watch = [1, 1, 1, 1, 1, 0, 0]

ans = solution(watch)
print(ans)