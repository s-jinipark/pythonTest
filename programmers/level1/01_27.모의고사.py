def solution(answers):
    answer = []
    std1 = [1, 2, 3, 4, 5]  # 5개 반복
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개 반복
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  #10개 반복

    score = [0] * 3
    idx = [0] * 3

    for i in range(len(answers)):
        #print(answers[i])
        # answers 가 5개 이상, 8 이상 일 때의 처리...
        if i % 5 == 0 :
            idx[0] = 0
        elif i % 8 == 0 :
            idx[1] = 0
        elif i % 10 == 0 :
            idx[2] = 0
        print(answers[i], std3[idx[2]])

        if answers[i] == std1[idx[0]] :
            score[0] += 1
        if answers[i] == std2[idx[1]] :
            score[1] += 1
        if answers[i] == std3[idx[2]] :
            score[2] += 1

        idx[0] += 1
        idx[1] += 1
        idx[2] += 1
    print(score)
    top_score = max(score)
    print(top_score)
    for i in range(len(score)):
        if score[i] == top_score :
            answer.append(i+1)
    answer.sort()

    return answer

#ans = [1,2,3,4,5]
ans = [1,3,2,4,2]
re = solution(ans)
print(re)

print("====================")
