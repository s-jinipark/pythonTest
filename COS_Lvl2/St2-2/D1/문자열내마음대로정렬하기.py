def solution(strings, n):
    answer = []

    for i in range(len(strings)):
        #print(strings[i][n])
        for j in range(len(strings)-1) :
            #print(strings[j][n], ' / ', strings[j+1][n])
            if strings[j][n] > strings[j+1][n] :
                tmp = strings[j]
                strings[j] = strings[j+1]
                strings[j + 1] = tmp
            elif strings[j][n] == strings[j+1][n] :
                if strings[j][n+1:] > strings[j+1][n+1:] :
                    tmp = strings[j]
                    strings[j] = strings[j + 1]
                    strings[j + 1] = tmp

    for s in strings :
        answer.append(s)
    return answer


# main 부분
strings = ["sun", "bed", "car"]
n = 1   # ["car", "bed", "sun"]
res = solution(strings, n)
print(res)

strings = ["abce", "abcd", "cdx"]
n = 2   # ["abcd", "abce", "cdx"]

res = solution(strings, n)
print(res)