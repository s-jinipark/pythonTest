def solution(seminars, t):
    st = 0
    total = 0
    answer = 0
    for ed in range(len(seminars)):
        total += seminars[ed]
        #while total >= t:
        while total > t:   # 웁스 여기 였음!
            total -= seminars[st]
            st += 1
            print(total, st)
        if total == t:
            answer += 1
    return answer

seminars = [1, 2, 3, 2, 5]
t = 5
ans= solution(seminars, t)
print('ans:', ans)


