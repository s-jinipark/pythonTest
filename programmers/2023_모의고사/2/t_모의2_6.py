def solution(n, bulbs):
    answer = 0
    light = [0 for _ in range(11)]
    print(light)
    for i in range(len(bulbs)):
        light[bulbs[i]] = 1 - light[bulbs[i]]
    print(light)

    for i in range(1, n + 1):
        if light[i] == 1:   # 변경  0 -> 1
            answer += 1
    return answer

n = 3
bulbs = [2,3,2]
ans= solution(n, bulbs)
print('ans:', ans)


