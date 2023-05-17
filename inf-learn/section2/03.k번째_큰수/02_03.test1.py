#[2]
from itertools import  combinations

# 프로그래머스 스타일 로 ...
def solution(N, K, nlist):
    answer = 0
    tmp = []
    # 3장 고정이니까, 루프 3번
    # for i in range(N):
    #     for j in range(N):
    #         for k in range(N):
    #             if i == j or j == k or k == i :
    #                 continue
    #             tmp.append(nlist[i]+nlist[j]+nlist[k])
    #
    # tmp.sort(reverse=True)
    # print(tmp)
    # answer = tmp[K-1]
    #
    # => 오우~! 이 거 안됨

    #[2] combinations 으로
    tmp = (list)(combinations(nlist, K))
    print(tmp)
    tmp2 = []
    for t in tmp:
        tmp2.append(t[0]+t[1]+t[2])
    print(tmp2)
    tmp2.sort(reverse=True)
    print(tmp2)
    answer = tmp2[K-1]
    return answer


N=10
K=3
nlist = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]
re = solution(N, K, nlist)
print(re)
#=>

