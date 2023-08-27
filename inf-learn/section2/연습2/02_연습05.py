
##### 정다면체
def solution():
    answer = 0
    # 두개 던지니까 이중 for 로 하고
    # 합계를 구한 뒤 --> dict 에 넣어서 갯수 셈
    # 마지막에 가장 큰 수 다 출력
    tmp = dict()
    for i in range(1, N+1):
        for j in range(1, M+1):
            #print(i, j)
            t = i +j
            if t not in tmp :
                tmp[t] = 1
            else :
                tmp[t] += 1
    #print(tmp, max(tmp))
    # 가장 많이 나온 수 의 (그 횟수, 확률)
    maxCnt = 0
    for t in tmp:  # k, v 구하는 법이 있을 터인데.
        print(t, tmp[t])
        if maxCnt < tmp[t]:
            maxCnt = tmp[t]
    print("maxCnt", maxCnt)
    t_lst = []
    for t in tmp:
        if tmp[t] == maxCnt:
            t_lst.append(t)
    print(t_lst)
    return answer
'''
풀이에서는 cnt => N, M 의 합의 빈도를 저장하는 배열

'''

N = 4  # N과 M 은 4,6,8,12,20 중 하나
M = 6
re = solution()
print(re)
#=> 5 6 7


N = 8
M = 12
re = solution()
print(re)
#=> 9 10 11 12 13
