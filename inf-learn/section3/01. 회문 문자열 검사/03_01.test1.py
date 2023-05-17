
# 프로그래머스 스타일 로 ...
def solution(N, inp):
    answer = 0
    res = ['YES'] * N
    print(res)
    for i in range(len(inp)):
        tmp = inp[i].lower()
        #print(len(i)//2)
        for j in range(len(tmp)//2):
            print(j, len(tmp)-1-j)
            if tmp[j] != tmp[len(tmp)-1-j] :
                res[i] = 'NO'
                break
    print(res)
    return answer

N = 5
inp = ['level', 'moon', 'abcba', 'soon','gooG']
re = solution(N, inp)
print(re)
#=>
