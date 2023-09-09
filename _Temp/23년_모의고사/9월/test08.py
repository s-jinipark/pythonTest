
def solution(dice):
    answer = 0
    for d in dice:
        #print(d)
        f, s = d
        print(f, s)
        if f == s :
            answer += f * 1000
        else :
            if f > s :
                answer += f * 500 + s *100
            else :
                answer += s * 500 + f * 100
    return answer


dice = [[3,3],[2,5]]

an = solution(dice)

print(an)