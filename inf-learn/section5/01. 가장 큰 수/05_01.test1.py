
# 프로그래머스 스타일 로 ...
def solution(M, inp):
    answer = 0
    stk = []
    # while inp > 0 :
    #     print(inp//10, inp%10)
    #     inp = inp//10
    tmp = str(inp)
    for i in range(len(tmp)):
        print(tmp[i])
        if len(stk) == 0 :
            stk.append(int(tmp[i]))
        else :  # 이제 값 비교

    return answer


M = 3

inp = 5276823


re = solution(M,inp)
print('re :', re)
#=> 3
print('==============================')

