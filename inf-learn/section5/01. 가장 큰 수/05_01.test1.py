
# 프로그래머스 스타일 로 ...
def solution(M, inp):
    answer = '' # 0
    stk = []
    # while inp > 0 :
    #     print(inp//10, inp%10)
    #     inp = inp//10

    # 스트링으로 하는 게 나을 듯
    tmp = str(inp)
    cnt = 0
    for i in range(len(tmp)):
        print(tmp[i])

        if len(stk) == 0 :  # 비어 있으면 , 바로 넣는다
            stk.append(int(tmp[i]))
            continue

        # 이제 값 비교
        for j in range(len(stk)-1, -1, -1):
            print('>', stk[j])
            if stk[j] < int(tmp[i]) and M > cnt:
                stk.pop()
                cnt += 1

        stk.append(int(tmp[i]))

    # cnt 와 비교해서  자른다 (주의)
    print(M, cnt)
    while M > cnt :
        stk.pop()
        cnt += 1
    print(stk)

    for s in stk :
        answer += str(s)

    return answer


M = 3

inp = 5276823


re = solution(M,inp)
print('re :', re)
#=> 3
print('==============================')

M = 5

inp = 9977252641

re = solution(M,inp)
print('re :', re)
#=> 3
print('==============================')