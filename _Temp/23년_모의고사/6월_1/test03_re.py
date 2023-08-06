
def solution(anagram):
    answer = 0
    for i in range(len(anagram)):
        alpha = [0] * 26
        for j in range(len(anagram[i][0])):
            #print(anagram[i][0][j], ord(anagram[i][0][j])-ord('A'))
            if 'A' <= anagram[i][0][j] <= 'Z':
                alpha[ ord(anagram[i][0][j])-ord('A') ] += 1   # <- 빈칸
            elif 'a' <= anagram[i][0][j] <= 'z':
                alpha[ ord(anagram[i][0][j])-ord('a') ] += 1   # <- 빈칸
        print(alpha)

        for j in range(len(anagram[i][1])):
            if 'A' <= anagram[i][1][j] <= 'Z':
                alpha[ ord(anagram[i][1][j])-ord('A') ] -= 1   # <- 빈칸
            elif 'a' <= anagram[i][1][j] <= 'z':
                alpha[ ord(anagram[i][1][j])-ord('a') ] -= 1   # <- 빈칸
        print(alpha)

        check = 1
        for j in range(26):
            if  alpha[j] != 0:   # <- 빈칸
                check = 0
        if check == 1:
            answer += 1
    return answer

anagram = [["Dog","God"],["ate","cat"],["friend", "finder"]]

re = solution(anagram)
print(re)