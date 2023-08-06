
def solution(s, p):
    answer = 0

    for i in range(len(s) - len(p) + 1):
        check = 1
        for j in range(i, i + len(p) ):
            if s[j] != p[j-i]:
                check = 0
                break
        if check == 1:
            answer += 1

    return answer

s = "ABABA"
p = "ABA"

re = solution(s, p)
print(re)