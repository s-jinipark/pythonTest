
##### 정다면체
def solution():
    answer = 0
    tmp = dict()
    for i  in range(1, N+1):
        for j in range(1, M+1):
            #print(i, j)
            t_sum = i + j
            if t_sum not in tmp:
                tmp[t_sum] = 0
            tmp[t_sum] += 1
    #print(연습, max(연습))

    # 풀다 말았는데, 계속...
    #-> 갯수를 세서 dict 에 넣었고..
    # => 5,6,7 이 각각 4 로 top 임

    # - 최대값을 찾아야 함.
    # - 최대값을 가지는 key 출력
    max_val = 0
    for t in tmp:
        #print(t, 연습[t])
        if tmp[t] > max_val:
            max_val = tmp[t]
    res = []
    for tv in tmp:
        if tmp[tv] == max_val:
            #print(tv)
            res.append(tv)
    print(res)
    return answer

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
