def solution(k, m, score):
    answer = 0
    score.sort()
    print(score)
    tmp_sum = 0
    minVal = 0
    while len(score) >= m :
        tmp = score[-m:]
        minVal = min(tmp)
        for i in range(m):
            score.pop()
        print(score, tmp, minVal, minVal * m)
        tmp_sum += minVal * m
        print(tmp_sum)
        answer = tmp_sum
    return answer

#k = 3
#m = 4
#score = [1, 2, 3, 1, 2, 3, 1]
k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

re = solution(k, m, score)
print(re)

