def solution(strings, n):
    answer = []
    avata = []
    for s in strings:
        print(s[n])  # n 은 인덱스
        avata.append(s[n])
        answer.append(s)
    print(avata)

    # 버블 가보자
    for i in range(len(avata)) :
        for j in range(i+1, len(avata)):
            print(avata[i], avata[j])
            #print(avata[i] > avata[j] )
            if avata[i] > avata[j] :
                tmp = avata[j]
                tmp2 = answer[j]
                avata[j] = avata[i]
                answer[j] = answer[i]
                avata[i] = tmp
                answer[i] = tmp2
            elif avata[i] == avata[j]:
                if answer[i] > answer[j] : # 동일하다면 원본으로 비교
                    tmp2 = answer[j]
                    answer[j] = answer[i]
                    answer[i] = tmp2
    print(avata, answer)

    return answer

#arr = ["sun", "bed", "car"]
arr = ["abce", "abcd", "cdx"]
#n = 1
n = 2

re = solution(arr, n)
print(re)

print("====================")

# 람다를 익혀두자

def solution2(strings, n):
    answer = []
    avata = []
    for s in strings:
        answer.append(s)
    print(answer)

    answer.sort(key= lambda x : (x[n], x))
    return answer

re2 = solution2(arr, n)
print(re2)