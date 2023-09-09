
##### 두 리스트 합치기
def solution():
    answer = 0
    tmp = []
    tmp = inp1 + inp2
    print(tmp)
    tmp.sort()
    print(tmp)
    # 문제에서 원하는 건 이게 아님

    # 이 문제 스타일을 알고 있어야 (괄호를 넣을 수 있음)
    idx1 = 0
    idx2 = 0
    tmp = []
    while  idx1 < N and idx2 < M:
        if inp1[idx1] < inp2[idx2]:
            tmp.append(inp1[idx1])
            idx1 += 1
        else:
            tmp.append(inp2[idx2])
            idx2 += 1
    print(tmp)
    if idx1 < N :
        tmp += inp1[idx1:]
    if idx2 < M:
        tmp += inp2[idx2:]
    print(tmp)
    return answer

N=3
inp1 = [1,3,5]
M=5
inp2 = [2,3,6,7,9]
re = solution()
print(re)
#=>
