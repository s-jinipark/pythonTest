

def solution(typo):
    answer = []
    for t in typo :
        tmp = t[0]
        print(t, tmp[int(t[1])])
        front = tmp[:int(t[1])]
        end = tmp[int(t[1])+1:]
        print(front, end)
        answer.append(front+end)
    return answer


typo = [["appple", "1"],["bananaa", "6"]]


an = solution(typo)
print(an)