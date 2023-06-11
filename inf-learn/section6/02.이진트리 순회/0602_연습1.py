

def DFS(v, N):
    #global rtn

    if N > 7 :  # 종료 조건 ?
        return
    else :
        #print(N)  # 전위순회 출력 : 1 2 4 5 3 6 7
        DFS(v + 1, N * 2)
        #print(N)  # 중위순회 출력 : 4 2 5 1 6 3 7
        DFS(v + 1, (N * 2)+1)
        print(N)  # 후위순회 출력 : 4 5 2 6 7 3 1


def solution(N):
    answer = 0

    DFS(0, 1)   # 1부터 가야지?

    return answer

N = 7  # N 까지 순회하는 걸로
#rtn = ''

re = solution(N)
print('re :', re)

#print(rtn)

'''
여기선 v (레벨)  은 필요 없고,
N 만 있으면 된다는


'''