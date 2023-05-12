def solution(n):
    answer = []
    tmp_s = str(n)
    for i in range(len(tmp_s), 0, -1):
        answer.append(int(tmp_s[i-1]))
    return answer

n = 12345

re = solution(n)
print(re)

print("====================")

