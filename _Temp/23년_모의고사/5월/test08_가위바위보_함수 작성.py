
def solution(gawibawibo):
    answer = []

    # 결국 2명이 하는거 아님?
    answer.append(0)
    answer.append(0)
    print(answer)
    n = len(gawibawibo[0])

    for i in range(n):
        #가위는 2, 바위는 0, 보자기는 5로 표현
        print(gawibawibo[0][i], gawibawibo[1][i])
        a = gawibawibo[0][i]
        b = gawibawibo[1][i]
        # a 가 이기는 것만 고려
        if (a == 2 and b == 5) or (a == 0 and b == 2) or (a == 5 and b == 0) :
            answer[0] +=1
        elif a == b :
            continue
        else :
            answer[1] += 1

    #print(n)

    return answer


#gawibawibo = [[2, 0, 5], [5, 0, 2]]
gawibawibo =[[2, 2, 0], [5, 5, 2]]

an = solution(gawibawibo)
print('an = ', an)

