
# 프로그래머스 스타일 로 ...
def solution(N, inp):
    answer = 0

    tmp = [0]*N

    for i in range(N):
        for j in range(N):
            if (inp[i]==0 and tmp[j]==0):  # 둘다 0 이면 바로 넣는다
                #print(inp[i], 연습[j])
                tmp[j] = i+1  # + 1 해야 된다는 점
                break
            elif tmp[j]==0 :
                #print(inp[i], 연습[j])
                inp[i] -= 1  # 순서를 표시하는 키 !
                # 순서를 건너뛰는 효과, 이게 사전 준비 없이 생각 날 수 있나?
                print('>', inp[i])
        print(tmp)
    return answer

N = 8

inp = [5, 3, 4, 0, 2, 1, 1, 0]

re = solution(N, inp)
print('re :', re)
#=>
print('==============================')

