from itertools import combinations

def solution(number):
    answer = 0
    tmp = list(combinations(number, 3))
    print(tmp)
    for t in tmp:
        print(sum(t))
        if sum(t) == 0 :
            answer += 1

    return answer


number = [-2, 3, 0, 2, -5]

re = solution(number)
print(re)

