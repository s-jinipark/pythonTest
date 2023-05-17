
# 프로그래머스 스타일 로 ...
def solution(N, nlist):
    answer = 0
    n_avg = 0
    sum = 0
    tmp = [0] *N
    for l in nlist:
        sum += l
    n_avg = round(sum/N)
    print(n_avg)  # 평균(소수 첫째자리 반올림)
    #print(tmp)
    for j in range(N):
        tmp[j] = abs( nlist[j]-n_avg)

    print(tmp)
    minVal = 2147000000
    min_idx = 0
    for k in range(N):
        if minVal > tmp[k]:
            minVal = tmp[k]
            min_idx = k
        elif minVal == tmp[k]:
            if nlist[min_idx] < nlist[k] :
                min_idx = k
    answer = min_idx+1  # 마지막에 +1 해서 1부터 시작하는 것으로...
    return answer


N=10
nlist = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
re = solution(N, nlist)
print(re)
#=>

