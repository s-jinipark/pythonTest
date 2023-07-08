
# 프로그래머스 스타일 로 ...
def solution(N, inp):
    answer = 0

    tmp = [0]*N
    #print(연습)

    for i in range(len(inp)):
        print(inp[i])
        # val 이 5 면 , 앞에 5칸이 있음
        # 앞에서 부터 0 이 5 개 있고 다음에 넣으면 되는데
        # 이때 0 이 아니면 다음, 다음으로 ... 넘어감
        # 넣을 때는 i + 1 로 넣는다

        # if 연습[inp[i]] == 0 :
        #     연습[inp[i]] = i +1
        # else :
        #     # 만약에 0 이 아니다... 그럼 다음 숫자로...
        #     cnt = i
        #     for j in range(cnt, N-1):
        #         cnt += 1
        #         if 연습[cnt] == 0 :
        #             연습[cnt] = i +1
        #             break

        cnt = 0
        stop = False
        for j in range(len(tmp)):
            if tmp[j] == 0 :
                 cnt += 1
            # # 앞에 0 계산
            if cnt == inp[i] :
                print(cnt, j)
                for k in range(j+1, len(tmp)):
                    if tmp[k] == 0 :
                        tmp[k] = i + 1
                    else :
                        break
                        stop =True
            if stop :
                cnt = 0
                stop = False
                break
        print(tmp)

    return answer

N = 8

inp = [5, 3, 4, 0, 2, 1, 1, 0]

re = solution(N, inp)
print('re :', re)
#=>
print('==============================')

