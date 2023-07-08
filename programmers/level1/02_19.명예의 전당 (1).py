def solution(k, score):
    answer = []
    tmp = [-1] * k
    print(tmp)

    for s in score :
        for i in range(k):
            #print(s, 연습, min(연습))

            if s > tmp[i]  and min(tmp) == tmp[i]:   # 작은 값 중에, 최소 값인 곳
                tmp[i] = s
                break
        # print('>', min(연습))
        # print(s, 연습, min(연습))
        # answer.append(min(연습))
        minVal = 99999
        for j in range(len(tmp)) :
            if minVal > tmp[j] and tmp[j] > -1 :
                minVal = tmp[j]
        print(minVal)
        answer.append(minVal)
    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]

re = solution(k, score)
print(re)

