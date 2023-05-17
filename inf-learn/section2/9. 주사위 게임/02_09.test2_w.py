
def solution(N, su_lst):
    answer = 0
    sum = 0
    maxVal = 0
    # 3개의 주사위 고정
    for s in su_lst:
        print(s)
        if s[0] == s[1] and s[1] == s[2] and s[2] == s[0] :
            sum = 10000 + (s[0]*1000)
        elif s[0] == s[1]  or s[2] == s[0]:
            sum = 1000 + (s[0] * 100)
        elif s[1] == s[2] :
            sum = 1000 + (s[1] * 100)
        else :
            #print(max(s))
            sum = max(s) * 100
        print(sum)
        if maxVal < sum :
            maxVal = sum
    answer = maxVal
    return answer

N = 3
su_lst = [[3, 3, 6],[2, 2, 2],[6, 2, 5]]

re = solution(N, su_lst)
print(re)
print('====================')
