
# 프로그래머스 스타일 로 ...
def solution(inp):
    answer = 0
    tmp = ''
    for i in inp:
        #print(i, i.isnumeric())
        if i.isnumeric():
            tmp += i
    print(tmp, int(tmp))
    i_tmp = int(tmp)
    for j in range(1, i_tmp+1):
        #print(j)
        if i_tmp %j == 0 :
            answer += 1
    return answer


inp = 'g0en2Ts8eSoft'
re = solution(inp)
print(re)
#=>
