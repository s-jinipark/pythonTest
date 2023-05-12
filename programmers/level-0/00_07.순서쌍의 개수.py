def solution(n):
    answer = 0
    start = 1
    end = n
    for i in range(start, end+1):
        for j in range(end, start-1, -1):
            if i * j == n :
                print(i, j)
                answer += 1
                #start = i     # <= *** 여기 중요
                end = j
                break
    return answer

n = 20

re = solution(n)

print(re)
print("====================")

