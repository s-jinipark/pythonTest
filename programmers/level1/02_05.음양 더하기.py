def solution(absolutes, signs):
    #answer = 123456789
    answer = 0

    for i in range(len(absolutes)) :
        print(absolutes[i])
        if signs[i] :
            answer += absolutes[i]
        else :
            answer += (absolutes[i] * -1)
    return answer

absolutes = [4,7,12]
signs = [True,False,True]

re = solution(absolutes, signs)
print(re)



