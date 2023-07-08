
##### 두 리스트 합치기
def solution():
    answer = 0
    tmp = inp1 + inp2
    tmp.sort()
    print(tmp)

    # 위 처럼 하면 안되고...
    # 기출 임
    c = []
    idx1 = 0
    idx2 = 0
    len1 = len(inp1)
    len2 = len(inp2)

    while idx1 < len1 and idx2 < len2 :
        if inp1[idx1]  < inp2[idx2] :
            c.append(inp1[idx1])
            idx1 += 1
        else :
            c.append(inp2[idx2])
            idx2 += 1
    print(c)
    # 나머지 처리
    if idx1 < len1-1:
        c = c + inp1[idx1:]
    if idx2 < len2-1:
        c = c + inp2[idx2:]
    print(c)
    return answer

N=3
inp1 = [1,3,5]
M=5
inp2 = [2,3,6,7,9]
re = solution()
print(re)
#=>
