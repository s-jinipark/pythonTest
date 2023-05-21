
def check_hm(t):
    # 5자리 고정이므로
    if t[0] == t[4] and t[1] == t[3]:
        return True
    else :
        return False

# 프로그래머스 스타일 로 ...
def solution(inp):
    answer = 0

    # 직선만 대상이니까
    # 행으로 한 번 검색하고, 다음으로 열로 검색
    len_inp = len(inp)

    for i in range(len_inp):
        print(inp[i])
        for j in range(0, len_inp-5+1):
            #print(j)
            tmp = []
            for k in range(j,j+5):
                #print('>', k)
                tmp.append(inp[i][k])
            #print(tmp)
            if check_hm(tmp):
                answer += 1

    # 다음으로 열로 검색
    for i in range(len_inp):
        #print(inp[i])
        for j in range(0, len_inp-5+1):
            #print(j)
            tmp = []
            for k in range(j,j+5):
                #print('>', k)
                tmp.append(inp[k][i])   # *** 여기만 변경
            print(tmp)
            if check_hm(tmp):
                answer += 1
    return answer

inp = [
[2,4,1,5,3,2,6],
[3,5,1,8,7,1,7],
[8,3,2,7,1,3,8],
[6,1,2,3,2,1,1],
[1,3,1,3,5,3,2],
[1,1,2,5,6,5,2],
[1,2,2,2,2,1,5]
]

re = solution(inp)
print('re :', re)
#=>
print('==============================')
