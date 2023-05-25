
# 프로그래머스 스타일 로 ...
def solution(N, inp):
    answer = 0

    tmp = [0]*N

    for i in range(N):
        for j in range(N):
            if (inp[i]==0 and tmp[j]==0):  # 둘다 0 이면 바로 넣는다
                #print(inp[i], tmp[j])
                tmp[j] = i+1
                break
            elif tmp[j]==0 :
                #print(inp[i], tmp[j])
                inp[i] -= 1  # 순서를 표시하는 키 !
                print('>', inp[i])
        print(tmp)
    return answer

N = 8

inp = [5, 3, 4, 0, 2, 1, 1, 0]

re = solution(N, inp)
print('re :', re)
#=>
print('==============================')

